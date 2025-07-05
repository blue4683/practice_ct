from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx):
    dist = 0
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        dist = max(dist, visited[y][x] - 1)
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == 'W' or visited[yy][xx]:
                continue

            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))

    return dist


n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
result = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] == 'W':
            continue

        result = max(result, bfs(y, x))

print(result)
