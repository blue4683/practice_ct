import sys
input = sys.stdin.readline
MOD = 10 ** 9

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(k + 1):
    dp[0][i] = 1

for x in range(1, n + 1):
    for y in range(1, k + 1):
        for z in range(x + 1):
            dp[x][y] += dp[z][y - 1]

        dp[x][y] %= MOD

print(dp[n][k])
