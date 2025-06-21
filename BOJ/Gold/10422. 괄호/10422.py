import sys
input = sys.stdin.readline
MOD = 1000000007

dp = [0] * 2501
dp[0] = 1
dp[1] = 1
for i in range(2, 2501):
    for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j]
        dp[i] %= MOD

for _ in range(int(input())):
    l = int(input())
    print(dp[l // 2]) if not l % 2 else print(0)
