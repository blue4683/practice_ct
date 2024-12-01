from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def activate(pos, arr):
    q = deque()
    for y, x in pos:
        arr[y][x] = 0
        q.append((y, x))

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == -1 or arr[yy][xx] <= arr[y][x] + 1:
                continue

            arr[yy][xx] = arr[y][x] + 1
            q.append((yy, xx))

    time = 0
    for y in range(n):
        for x in range(n):
            if (y, x) in virus:
                continue

            if arr[y][x] == INF:
                return INF

            time = max(time, arr[y][x])

    return time


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
virus = set((y, x) for y in range(n) for x in range(n) if lab[y][x] == 2)

result = INF
cases = combinations(virus, m)
visited = [list(map(lambda x: -1 if x == 1 else INF, arr)) for arr in lab]
for pos in cases:
    result = min(result, activate(pos, [arr[:] for arr in visited]))

print(-1) if result == INF else print(result)
