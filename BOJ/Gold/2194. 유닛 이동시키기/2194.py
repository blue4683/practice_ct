from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 10 ** 9


def out_of_range(y, x):
    if y < 0 or y > n - a or x < 0 or x > m - b:
        return 1

    return 0


def is_block(y, x):
    for dy in range(a):
        for dx in range(b):
            if arr[y + dy][x + dx] == -1:
                return 1

    return 0


def bfs():
    q = deque([(sy, sx)])
    arr[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if (y, x) == (ey, ex):
            return arr[y][x]

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] <= arr[y][x] + 1 or is_block(yy, xx):
                continue

            arr[yy][xx] = arr[y][x] + 1
            q.append((yy, xx))

    return -1


n, m, a, b, k = map(int, input().split())
arr = [[INF] * (m) for _ in range(n)]
for _ in range(k):
    y, x = map(lambda x: int(x) - 1, input().split())
    arr[y][x] = -1

sy, sx = map(lambda x: int(x) - 1, input().split())
ey, ex = map(lambda x: int(x) - 1, input().split())

print(bfs())
