import sys
input = sys.stdin.readline


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for y in range(n):
    for x in range(n):
        k = arr[y][x]
        if not k:
            continue

        yy, xx = y + k, x + k
        if not out_of_range(yy, x):
            dp[yy][x] += dp[y][x]

        if not out_of_range(y, xx):
            dp[y][xx] += dp[y][x]

print(dp[-1][-1])
