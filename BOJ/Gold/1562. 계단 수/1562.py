import sys
input = sys.stdin.readline
MOD = 10 ** 9

n = int(input())

if n < 10:
    print(0)

else:
    dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n)]
    for k in range(1, 10):
        dp[0][k][1 << k] = 1

    for i in range(1, n):
        for k in range(10):
            for bit in range(1 << 10):
                if k - 1 >= 0:
                    dp[i][k][bit | (1 << k)] += dp[i - 1][k - 1][bit]

                if k + 1 < 10:
                    dp[i][k][bit | (1 << k)] += dp[i - 1][k + 1][bit]

                dp[i][k][bit | (1 << k)] %= MOD

    result = 0
    for k in range(10):
        result += dp[n - 1][k][1023]
        result %= MOD

    print(result)
