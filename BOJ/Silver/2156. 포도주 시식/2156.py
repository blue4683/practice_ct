import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][1] = wines[0]

for i in range(1, n):
    dp[i][0] = max(dp[i][0], max(dp[i - 1]))
    for j in range(1, 3):
        if j != 1 and not dp[i - 1][j - 1]:
            continue

        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + wines[i])

print(max(dp[n - 1]))
