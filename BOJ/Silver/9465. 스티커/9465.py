import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    for x in range(1, n):
        dp[0][x] = max(dp[0][x], dp[0][x - 1], dp[1][x - 1],
                       dp[1][x - 1] + stickers[0][x])
        dp[1][x] = max(dp[1][x], dp[0][x - 1], dp[1][x - 1],
                       dp[0][x - 1] + stickers[1][x])

    print(max(dp[0][n - 1], dp[1][n - 1]))
