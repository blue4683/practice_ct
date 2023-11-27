import sys

input = sys.stdin.readline


def change_temp(temp, target):
    return min(10 - abs(temp - target), abs(temp - target))


n = int(input())
food = list(map(int, input().split()))

dp = [[[[int(1e9)] * 10 for _ in range(10)] for _ in range(10)] for _ in range(n + 1)]

dp[0][0][0][0] = 0

for i in range(n):
    for x in range(10):
        for y in range(10):
            for z in range(10):
                # if dp[i][x][y][z] == int(1e9):
                #     continue
                dp[i + 1][food[i]][y][z] = min(
                    dp[i + 1][food[i]][y][z],
                    dp[i][x][y][z] + change_temp(x, food[i]),
                )
                dp[i + 1][x][food[i]][z] = min(
                    dp[i + 1][x][food[i]][z],
                    dp[i][x][y][z] + change_temp(y, food[i]),
                )
                dp[i + 1][x][y][food[i]] = min(
                    dp[i + 1][x][y][food[i]],
                    dp[i][x][y][z] + change_temp(z, food[i]),
                )

result = 1e9

for x in range(10):
    for y in range(10):
        for z in range(10):
            result = min(result, dp[n][x][y][z])

print(result)
