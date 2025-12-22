import sys
input = sys.stdin.readline


def dfs(y, x):
    global result
    if y == n + 1 and x == 1:
        result += 1
        return

    if x == m:
        yy, xx = y + 1, 1

    else:
        yy, xx = y, x + 1

    if not (arr[y - 1][x] and arr[y][x - 1] and arr[y - 1][x - 1]):
        arr[y][x] = 1
        dfs(yy, xx)
        arr[y][x] = 0

    dfs(yy, xx)


n, m = map(int, input().split())

result = 0
arr = [[0] * (m + 1) for _ in range(n + 1)]
dfs(1, 1)

print(result)
