import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= 5 or x < 0 or x >= 9:
        return 1

    return 0


def dfs(depth, pins):
    global result
    result = min(result, (len(pins), depth))
    for y, x in pins:
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            yyy, xxx = yy + dy, xx + dx
            if out_of_range(yy, xx) or arr[yy][xx] != 'o' or out_of_range(yyy, xxx) or arr[yyy][xxx] != '.':
                continue

            arr[y][x] = '.'
            arr[yy][xx] = '.'
            arr[yyy][xxx] = 'o'
            dfs(depth + 1, (pins - {(y, x), (yy, xx)}) | {(yyy, xxx)})
            arr[yyy][xxx] = '.'
            arr[yy][xx] = 'o'
            arr[y][x] = 'o'


n = int(input())
for t in range(n):
    arr = [list(input().rstrip()) for _ in range(5)]
    pins = {(y, x) for y in range(5) for x in range(9) if arr[y][x] == 'o'}
    result = (8, 10 ** 9)
    dfs(0, pins)

    print(*result)
    if t != n - 1:
        input()
