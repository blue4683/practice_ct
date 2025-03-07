import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (h + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    dp[i] = dp[i - 1][:]
    for block in students[i - 1]:
        for j in range(block, h + 1):
            dp[i][j] += dp[i - 1][j - block]

print(dp[n][h] % 10007)
