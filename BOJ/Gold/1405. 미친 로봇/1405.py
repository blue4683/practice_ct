import sys
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(depth, y, x):
    global result
    if depth == n:
        result += arr[y][x]
        return

    for i in range(4):
        if not prop[i]:
            continue

        dy, dx = d[i]
        yy, xx = y + dy, x + dx
        if arr[yy][xx] != 0:
            continue

        arr[yy][xx] = arr[y][x] * prop[i]
        dfs(depth + 1, yy, xx)
        arr[yy][xx] = 0


n, *prop = map(int, input().split())
prop = list(map(lambda x: x / 100, prop))
arr = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
result = 0
arr[n][n] = 1
dfs(0, n, n)

print(result)
