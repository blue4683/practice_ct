from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx, is_row):
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        r = (0, 1) if is_row else (2, 3)
        for i in r:
            dy, dx = d[i]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx] != arr[sy][sx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))


n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

result = 0
visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if visited[y][x]:
            continue

        result += 1
        visited[y][x] = 1
        bfs(y, x, arr[y][x] == '-')

print(result)
