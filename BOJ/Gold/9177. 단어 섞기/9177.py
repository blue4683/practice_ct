import sys
input = sys.stdin.readline


def dfs(y, x):
    if y == n and x == m:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    if y < n and a[y] == c[y + x] and dfs(y + 1, x):
        dp[y][x] = 1
        return dp[y][x]

    if x < m and b[x] == c[y + x] and dfs(y, x + 1):
        dp[y][x] = 1
        return dp[y][x]

    dp[y][x] = 0
    return dp[y][x]


for t in range(1, int(input()) + 1):
    a, b, c = input().split()
    n, m = map(len, [a, b])
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    result = 'yes' if dfs(0, 0) else 'no'

    print(f'Data set {t}: {result}')
