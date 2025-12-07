from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def bfs(sy, sx):
    global a, b
    o, v = 0, 0
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        if arr[y][x] == 'v':
            v += 1

        elif arr[y][x] == 'o':
            o += 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == '#' or visited[yy][xx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    if o > v:
        a += o

    else:
        b += v


r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

visited = [[0] * c for _ in range(r)]
a, b = 0, 0
for y in range(r):
    for x in range(c):
        if arr[y][x] == '#' or visited[y][x]:
            continue

        visited[y][x] = 1
        bfs(y, x)

print(a, b)
