import sys
input = sys.stdin.readline
INF = 10 ** 9

n = int(input())
matrixes = [list(map(int, input().split())) for _ in range(n)]

dp = [[INF] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for i in range(2, n + 1):
    for j in range(n - i + 1):
        for k in range(j, j + i - 1):
            dp[j][j + i - 1] = min(dp[j][j + i - 1], dp[j][k] + dp[k + 1]
                                   [j + i - 1] + matrixes[j][0] * matrixes[k][1] * matrixes[j + i - 1][1])

print(dp[0][n - 1])
