from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def numbering_island(sy, sx, number):
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        visited[y][x] = number
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or mapp[yy][xx] != 'x' or visited[yy][xx] != -1:
                continue

            q.append((yy, xx))


def bfs(island, number):
    local_visited = [visited[i][:] for i in range(n)]
    is_outside = 0
    adj = set()
    q = [island]
    while q:
        y, x = q.pop()
        for dy, dx in d[:4]:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                is_outside = 1

            elif local_visited[yy][xx] == -1:
                local_visited[yy][xx] = number
                q.append((yy, xx))

            elif local_visited[yy][xx] != number:
                adj.add(local_visited[yy][xx])

    return is_outside, adj


def get_height(num, visited):
    islands = []
    for island in heights[num]:
        if visited[island]:
            continue

        visited[island] = 1
        islands.append(island)

    for island in islands:
        result[num] = max(result[num], get_height(island, visited) + 1)

    return result[num]


n, m = map(int, input().split())
mapp = [list(input().rstrip()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
islands = []

number = 0
for y in range(n):
    for x in range(m):
        if mapp[y][x] == 'x' and visited[y][x] == -1:
            numbering_island(y, x, number)
            islands.append((y, x))
            number += 1

if not number:
    print(-1)
    exit()

number = len(islands)
outside = []
heights = defaultdict(set)
for num in range(number):
    is_outside, adj = bfs(islands[num], num)
    if is_outside:
        outside.append(num)

    heights[num] = adj

for i in range(number):
    for j in heights[i]:
        heights[j].add(i)

result = [0] * number
for island in outside:
    get_height(island, [x in outside for x in range(number)])

counter = Counter(result)
answer = []
for key in sorted(counter.keys()):
    if counter[key]:
        answer.append(counter[key])

print(*answer)
