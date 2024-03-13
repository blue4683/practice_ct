import sys
input = sys.stdin.readline


def mission(now, status):
    if now == n:
        return 1.0

    if dp[status] != -1:
        return dp[status]

    dp[status] = 0
    for i in range(n):
        if status & (1 << i) == 0:
            dp[status] = max(dp[status], rates[now][i]
                             * mission(now + 1, status | (1 << i)) / 100)

    return dp[status]


n = int(input())
rates = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (1 << n)

print(f"{mission(0, 0) * 100:.6f}")
