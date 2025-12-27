from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def bfs(sy, sx):
    cnt = 1
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx] != arr[sy][sx]:
                continue

            visited[yy][xx] = 1
            cnt += 1
            q.append((yy, xx))

    return cnt ** 2


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

b, w = 0, 0
for y in range(m):
    for x in range(n):
        if visited[y][x]:
            continue

        if arr[y][x] == 'W':
            w += bfs(y, x)

        else:
            b += bfs(y, x)

print(w, b)
