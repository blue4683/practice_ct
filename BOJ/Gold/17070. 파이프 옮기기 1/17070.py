import sys
input = sys.stdin.readline
d = [(0, 1), (1, 1), (1, 0)]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for y in range(n):
    for x in range(n):
        if arr[y][x] or (y, x) == (0, 0):
            continue

        for i in range(3):
            if i == 1 and (arr[y - 1][x] or arr[y][x - 1]):
                continue

            for j in range(3):
                if abs(i - j) == 2:
                    continue

                dy, dx = d[i]
                yy, xx = y - dy, x - dx
                if yy < 0 or xx < 0:
                    continue

                dp[y][x][i] += dp[yy][xx][j]

print(sum(dp[n - 1][n - 1]))
