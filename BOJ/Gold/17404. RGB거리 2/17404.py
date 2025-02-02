import sys
input = sys.stdin.readline
INF = 10 ** 9

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = INF
dp = [[INF] * 3 for _ in range(n)]
for color in range(3):
    for i in range(3):
        if color == i:
            dp[0][i] = graph[0][i]

        else:
            dp[0][i] = INF

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][2]

    for i in range(3):
        if i == color:
            continue

        result = min(result, dp[n - 1][i])

print(result)
