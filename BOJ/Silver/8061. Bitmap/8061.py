from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(pos):
    for y, x in pos:
        visited[y][x] = 0

    q = deque(pos)
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] <= visited[y][x] + 1:
                continue

            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))


n, m = map(int, input().split())
bitmap = [list(map(int, list(input().rstrip()))) for _ in range(n)]
pos = [(y, x) for y in range(n) for x in range(m) if bitmap[y][x]]
visited = [[INF] * m for _ in range(n)]
bfs(pos)

for l in visited:
    print(*l)
