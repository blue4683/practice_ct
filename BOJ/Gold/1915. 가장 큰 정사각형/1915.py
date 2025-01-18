import sys
input = sys.stdin.readline


n, m = map(int, input().split())
dp = [list(map(int, list(input().rstrip()))) for _ in range(n)]

for y in range(1, n):
    for x in range(1, m):
        if dp[y][x] and dp[y - 1][x] and dp[y][x - 1] and dp[y - 1][x - 1]:
            dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1

print(max(map(max, dp)) ** 2)
