import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(1)

else:
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(2, int(i ** 0.5) + 1):
            dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)

    print(dp[n])
