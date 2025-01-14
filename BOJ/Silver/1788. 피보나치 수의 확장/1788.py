import sys
input = sys.stdin.readline
MOD = 10 ** 9

n = int(input())
if 0 <= n < 2:
    for _ in range(2):
        print(n)

else:
    m = n if n > 0 else -n
    dp = [0] * (m + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, m + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    if n < 0 and not m % 2:
        print(-1)

    else:
        print(1)

    print(dp[m])
