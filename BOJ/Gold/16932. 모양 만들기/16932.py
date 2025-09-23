from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx):
    cnt = 1
    visited[sy][sx] = 1
    pos = set()
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            if not arr[yy][xx]:
                pos.add((yy, xx))

            else:
                cnt += 1
                visited[yy][xx] = 1
                q.append((yy, xx))

    for y, x in pos:
        adj[y][x] += cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

adj = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if arr[y][x] and not visited[y][x]:
            bfs(y, x)

result = 0
for y in range(n):
    for x in range(m):
        result = max(result, adj[y][x] + 1)

print(result)
