import sys
input = sys.stdin.readline


def fill(now, status):
    if now == n * m and status == 0:
        return 1

    if now >= n * m:
        return 0

    if dp[now][status] != -1:
        return dp[now][status]

    dp[now][status] = 0

    if status & 1:
        dp[now][status] = fill(now + 1, status >> 1)

    else:
        dp[now][status] = fill(now + 1, status >> 1 | 1 << (m - 1))
        if now % m != m - 1 and status & 2 == 0:
            dp[now][status] += fill(now + 2, status >> 2)

    dp[now][status] %= 9901
    return dp[now][status]


n, m = map(int, input().split())

dp = [[-1] * (1 << 14) for _ in range(14 ** 2)]
print(fill(0, 0))
