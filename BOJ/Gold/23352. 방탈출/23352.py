from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx):
    q = deque([(0, sy, sx)])
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1
    max_dist, last = 0, arr[sy][sx]
    while q:
        dist, y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or not arr[yy][xx]:
                continue

            if dist + 1 > max_dist:
                max_dist = dist + 1
                last = arr[yy][xx]

            elif dist + 1 == max_dist:
                last = max(last, arr[yy][xx])

            visited[yy][xx] = 1
            q.append((dist + 1, yy, xx))

    return arr[sy][sx] + last, max_dist


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result, max_dist = 0, 0
for y in range(n):
    for x in range(m):
        if arr[y][x]:
            pwd, dist = bfs(y, x)
            if dist > max_dist:
                result, max_dist = pwd, dist

            elif dist == max_dist:
                result = max(result, pwd)

print(result)
