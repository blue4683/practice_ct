import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]
for x in range(1, m):
    dp[0][x] += dp[0][x - 1]

for y in range(1, n):
    left_to_right = dp[y][:]
    right_to_left = dp[y][:]
    for x in range(m - 1, -1, -1):
        if x == m - 1:
            right_to_left[x] += dp[y - 1][x]

        else:
            right_to_left[x] += max(dp[y - 1][x], right_to_left[x + 1])

    for x in range(m):
        if x == 0:
            left_to_right[x] += dp[y - 1][x]

        else:
            left_to_right[x] += max(dp[y - 1][x], left_to_right[x - 1])

    for x in range(m):
        dp[y][x] = max(left_to_right[x], right_to_left[x])

print(dp[n - 1][m - 1])
