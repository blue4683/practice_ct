import sys
input = sys.stdin.readline
MOD = 10 ** 9

n = int(input())
if n == 1:
    print(9)
    exit()

dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for k in range(2, n + 1):
    for i in range(10):
        if not i:
            dp[k][i] = dp[k - 1][i + 1]

        elif i == 9:
            dp[k][i] = dp[k - 1][i - 1]

        else:
            dp[k][i] = dp[k - 1][i - 1] + dp[k - 1][i + 1]

print(sum(dp[k]) % MOD)
