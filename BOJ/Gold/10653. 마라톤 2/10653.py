import sys
input = sys.stdin.readline
INF = 10 ** 9


def get_distance(a, b):
    y1, x1 = checkpoints[a]
    y2, x2 = checkpoints[b]
    return abs(y1 - y2) + abs(x1 - x2)


n, k = map(int, input().split())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = get_distance(i, j)

dp = [[INF] * (k + 1) for _ in range(n)]
dp[0][0] = 0

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + distances[i - 1][i]

for i in range(1, k + 1):
    dp[0][i], dp[1][i] = 0, dp[i - 1][1]
    dp[i][i] = distances[i][0]
    for j in range(1, n):
        for l in range(i, 0, -1):
            if j - l - 1 < 0:
                continue

            dp[j][i] = min(dp[j][i], dp[j - l - 1][i - l] +
                           distances[j - l - 1][j], dp[j - 1][i] + distances[j][j - 1])

print(dp[n - 1][k])
