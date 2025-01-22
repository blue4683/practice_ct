import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 3


def get_case(n, k):
    if n / k == 2:
        return 2

    if k == 1:
        return n

    if not dp[n][k]:
        dp[n][k] = (get_case(n - 1, k) + get_case(n - 2, k - 1)) % MOD

    return dp[n][k]


n = int(input())
k = int(input())

if n / 2 < k:
    print(0)

else:
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    print(get_case(n, k))
