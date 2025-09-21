from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx, virus):
    global result
    if result == 'YES':
        return

    arr = [l[:] for l in before]
    q = deque([(sy, sx)])
    visited[sy][sx] = 1
    arr[sy][sx] = virus
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx] != before[y][x]:
                continue

            visited[yy][xx] = 1
            arr[yy][xx] = virus
            q.append((yy, xx))

    if arr == after:
        result = 'YES'

    return


n, m = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]

if before == after:
    print('YES')

else:
    result = 'NO'
    visited = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if before[y][x] != after[y][x] and not visited[y][x]:
                bfs(y, x, after[y][x])

    print(result)
