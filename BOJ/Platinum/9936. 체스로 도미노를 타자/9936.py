import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
INF = int(-1e9)


def cover(idx, status, cnt):
    if cnt == 0:
        return 0

    if idx >= n * 3:
        return INF

    if dp[idx][status][cnt] != INF:
        return dp[idx][status][cnt]

    if status & 1:
        dp[idx][status][cnt] = cover(idx + 1, status >> 1, cnt)
    else:
        dp[idx][status][cnt] = cover(idx + 1, status >> 1, cnt)

        if idx + 3 < n * 3:
            dp[idx][status][cnt] = max(dp[idx][status][cnt], cover(
                idx + 1, status >> 1 | 4, cnt - 1) + chess[idx] + chess[idx + 3])

        if idx % 3 != 2 and not (status & 2):
            dp[idx][status][cnt] = max(dp[idx][status][cnt], cover(
                idx + 2, status >> 2, cnt - 1) + chess[idx] + chess[idx + 1])

    return dp[idx][status][cnt]


n, k = map(int, input().split())
chess = []
for _ in range(n):
    chess.extend(list(map(int, input().split())))

dp = [[[INF] * (k + 1) for _ in range(8)] for _ in range(3 * (n + 1))]
print(cover(0, 0, k))
