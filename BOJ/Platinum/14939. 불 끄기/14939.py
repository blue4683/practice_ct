import sys
input = sys.stdin.readline
INF = 1e9

d = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]


def out_range(y, x):
    if 0 <= y < 10 and 0 <= x < 10:
        return False

    return True


def toggle(y, x, arr):
    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if not out_range(yy, xx):
            arr[yy][xx] ^= 1

    return arr


def check(arr):
    for y in range(10):
        for x in range(10):
            if arr[y][x]:
                return False

    return True


arr = [list(input().rstrip()) for _ in range(10)]
lights = [list(map(lambda x: 1 if x == 'O' else 0, arr[i])) for i in range(10)]
result = INF

for bit in range(1 << 10):
    cnt = 0
    tmp = [light[:] for light in lights]

    for x in range(10):
        if bit & (1 << x):
            cnt += 1
            tmp = toggle(0, x, tmp)

    for y in range(1, 10):
        for x in range(10):
            if tmp[y - 1][x]:
                cnt += 1
                tmp = toggle(y, x, tmp)

    if check(tmp):
        result = min(result, cnt)

print(-1) if result == INF else print(result)
