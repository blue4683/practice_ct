import sys
input = sys.stdin.readline
MOD = 987654321

n = int(input())
if n <= 2:
    print(1)

else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 1
    for i in range(4, n + 1, 2):
        for j in range(2, n + 1, 2):
            if i - j < 0:
                break

            dp[i] += dp[i - j] * dp[j - 2]
            dp[i] %= MOD

    print(dp[n])
