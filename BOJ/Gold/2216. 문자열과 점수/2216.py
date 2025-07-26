import sys
input = sys.stdin.readline
INF = -10 ** 9


a, b, c = map(int, input().split())
x, y = input().rstrip(), input().rstrip()
n, m = map(len, [x, y])

dp = [[INF] * (m + 1) for _ in range(n + 1)]
dp[n][m] = 0
for i in range(n, -1, -1):
    for j in range(m, -1, -1):
        if i < n and j < m:
            dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + [c, a][x[i] == y[j]])

        if i < n:
            dp[i][j] = max(dp[i][j], dp[i + 1][j] + b)

        if j < m:
            dp[i][j] = max(dp[i][j], dp[i][j + 1] + b)

print(dp[0][0])
