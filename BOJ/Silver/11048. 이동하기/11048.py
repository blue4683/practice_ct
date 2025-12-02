import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = arr[0][0]

for y in range(n):
    for x in range(m):
        tmp = 0
        if (y - 1) >= 0 and (x - 1) >= 0:
            tmp = max(tmp, dp[y - 1][x - 1])

        if (y - 1) >= 0:
            tmp = max(tmp, dp[y - 1][x])

        if (x - 1) >= 0:
            tmp = max(tmp, dp[y][x - 1])

        dp[y][x] = arr[y][x] + tmp

print(dp[n - 1][m - 1])
