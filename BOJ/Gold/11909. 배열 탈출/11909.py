import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[10 ** 9] * n for _ in range(n)]
dp[0][0] = 0
for y in range(n):
    for x in range(n):
        if x + 1 < n:
            if arr[y][x] <= arr[y][x + 1]:
                dp[y][x + 1] = min(dp[y][x + 1], dp[y][x] +
                                   arr[y][x + 1] - arr[y][x] + 1)

            else:
                dp[y][x + 1] = min(dp[y][x + 1], dp[y][x])

        if y + 1 < n:
            if arr[y][x] <= arr[y + 1][x]:
                dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] +
                                   arr[y + 1][x] - arr[y][x] + 1)

            else:
                dp[y + 1][x] = min(dp[y + 1][x], dp[y][x])

print(dp[n - 1][n - 1])
