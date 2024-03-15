import sys
input = sys.stdin.readline


def fill(idx, status):
    if idx == h * w and not status:
        return 1

    if idx >= h * w:
        return 0

    if dp[idx][status] != -1:
        return dp[idx][status]

    dp[idx][status] = 0

    if status & (1 << 0):
        dp[idx][status] = fill(idx + 1, status >> 1)

    else:
        dp[idx][status] = fill(idx + 1, status >> 1 | 1 << (w - 1))
        if idx % w != w - 1 and status & (1 << 1) == 0:
            dp[idx][status] += fill(idx + 2, status >> 2)

    return dp[idx][status]


while 1:
    h, w = map(int, input().split())
    if (h, w) == (0, 0):
        exit()

    else:
        dp = [[-1] * (1 << 11) for _ in range(11 ** 2)]
        print(fill(0, 0))
