MOD = 10 ** 9

n = int(input())
if n < 2:
    print(0)

elif n < 3:
    print(1)

else:
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD

    print(dp[n])
