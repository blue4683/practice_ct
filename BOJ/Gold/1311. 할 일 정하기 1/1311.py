import sys
input = sys.stdin.readline
INF = 10 ** 9


def give(now, status):
    if now == n:
        return 0

    if dp[status] != INF:
        return dp[status]

    dp[status] = INF
    for i in range(n):
        if status & (1 << i) == 0:
            dp[status] = min(dp[status], arr[now][i] +
                             give(now + 1, status | (1 << i)))

    return dp[status]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [INF] * (1 << n)

print(give(0, 0))
