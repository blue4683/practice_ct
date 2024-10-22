import sys
input = sys.stdin.readline

m, n = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(m)]
dp = [0] * (m + 1)
dp[m] = 1

for x in range(n):
    tmp = [0] * (m + 1)
    big = 0
    for y in range(m):
        if grid[y][x] == 'B':
            big = y + 1

    small = m
    for y in range(m - 1, -1, -1):
        if grid[y][x] == 'R':
            small = y

    for y in range(m, -1, -1):
        if y < m:
            dp[y] += dp[y + 1]

        if y >= big and y <= small:
            tmp[y] = dp[y]

    dp = tmp

print(sum(dp))
