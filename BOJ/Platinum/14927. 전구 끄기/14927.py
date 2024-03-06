import sys
input = sys.stdin.readline
INF = 1e9

d = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]


def out_range(y, x):
    if 0 <= y < n and 0 <= x < n:
        return 0

    return 1


def toggle(y, x, arr):
    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if not out_range(yy, xx):
            arr[yy][xx] ^= 1

    return arr


def check(arr):
    for y in range(n):
        for x in range(n):
            if arr[y][x]:
                return 0

    return 1


n = int(input())
lights = [list(map(int, input().split())) for _ in range(n)]
result = INF

for bit in range(1 << n):
    cnt = 0
    arr = [light[:] for light in lights]
    for x in range(n):
        if bit & (1 << x):
            cnt += 1
            arr = toggle(0, x, arr)

    for y in range(1, n):
        for x in range(n):
            if arr[y - 1][x]:
                cnt += 1
                arr = toggle(y, x, arr)

    if check(arr):
        result = min(result, cnt)

print(result) if result != INF else print(-1)
