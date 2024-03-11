import sys
input = sys.stdin.readline


def get_score(a, b):
    if ord(a) > ord(b):
        a, b = b, a

    if a == 'A':
        if b == 'A':
            return 10

        elif b == 'B':
            return 8

        elif b == 'C':
            return 7

        elif b == 'D':
            return 5

        else:
            return 1

    elif a == 'B':
        if b == 'B':
            return 6

        elif b == 'C':
            return 4

        elif b == 'D':
            return 3

        else:
            return 1

    elif a == 'C':
        if b == 'C':
            return 3

        elif b == 'D':
            return 2

        else:
            return 1

    elif a == 'D':
        if b == 'D':
            return 2

        else:
            return 1

    else:
        return 0


def cut(idx, status):
    if idx >= n * m:
        return 0

    if dp[idx][status] != -1:
        return dp[idx][status]

    dp[idx][status] = max(0, cut(idx + 1, status >> 1))

    if status & (1 << 0):
        dp[idx][status] = max(dp[idx][status], cut(idx + 1, status >> 1))

    else:
        if idx + m < n * m and status & (1 << 0) == 0:
            dp[idx][status] = max(dp[idx][status], cut(
                idx + 1, status >> 1 | 1 << (m - 1)) + get_score(tofu[idx], tofu[idx + m]))

        if idx % m != m - 1 and status & (1 << 1) == 0:
            dp[idx][status] = max(dp[idx][status], cut(
                idx + 2, status >> 2) + get_score(tofu[idx], tofu[idx + 1]))

    return dp[idx][status]


n, m = map(int, input().split())
tofu = ''
for _ in range(n):
    tofu += input().rstrip()

dp = [[-1] * (1 << 14) for _ in range(14 ** 2)]
print(cut(0, 0))
