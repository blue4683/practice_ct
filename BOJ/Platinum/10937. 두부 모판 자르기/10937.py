import sys
input = sys.stdin.readline


def get_score(a, b):
    if ord(a) > ord(b):
        a, b = b, a

    if a == 'A':
        if b == 'A':
            return 100

        elif b == 'B':
            return 70

        elif b == 'C':
            return 40

        else:
            return 0

    elif a == 'B':
        if b == 'B':
            return 50

        elif b == 'C':
            return 30

        else:
            return 0

    elif a == 'C':
        if b == 'C':
            return 20

        else:
            return 0

    else:
        return 0


def cut(idx, status):
    if idx >= n ** 2:
        return 0

    if dp[idx][status] != -1:
        return dp[idx][status]

    dp[idx][status] = max(0, cut(idx + 1, status >> 1))

    if status & (1 << 0):
        dp[idx][status] = max(dp[idx][status], cut(idx + 1, status >> 1))

    else:
        if idx + n < n ** 2:
            dp[idx][status] = max(dp[idx][status], cut(
                idx + 1, status >> 1 | 1 << (n - 1)) + get_score(tofu[idx], tofu[idx + n]))

        if idx % n != n - 1 and status & (1 << 1) == 0:
            dp[idx][status] = max(dp[idx][status], cut(
                idx + 2, status >> 2) + get_score(tofu[idx], tofu[idx + 1]))

    return dp[idx][status]


n = int(input())
tofu = ''
for _ in range(n):
    tofu += input().rstrip()

dp = [[-1] * (1 << 11) for _ in range(12 ** 2)]
print(cut(0, 0))
