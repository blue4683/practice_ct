from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def bfs(sy, sx):
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        if y == m - 1:
            return 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    return 0


m, n = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(m)]
result = 0
visited = [[0] * n for _ in range(m)]
for x in range(n):
    if result:
        break

    if not visited[0][x] and not arr[0][x]:
        result = bfs(0, x)

print('YES') if result else print('NO')
