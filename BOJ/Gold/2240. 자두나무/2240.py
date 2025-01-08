import sys
input = sys.stdin.readline


t, w = map(int, input().split())
plums = [int(input()) for _ in range(t)]
dp = [[[0] * 3 for _ in range(w + 1)] for _ in range(t)]
if plums[0] == 1:
    dp[0][0][1] = 1

else:
    dp[0][1][2] = 1

for i in range(1, t):
    for j in range(w + 1):
        if j:
            if plums[i] == 1:
                dp[i][j][1] = max(dp[i - 1][j - 1][2], dp[i - 1][j][1]) + 1
                dp[i][j][2] = max(dp[i - 1][j - 1][1], dp[i - 1][j][2])

            else:
                dp[i][j][1] = max(dp[i - 1][j - 1][2], dp[i - 1][j][1])
                dp[i][j][2] = max(dp[i - 1][j - 1][1], dp[i - 1][j][2]) + 1

        else:
            if plums[i] == 1:
                dp[i][0][1] = dp[i - 1][0][1] + 1
                dp[i][0][2] = dp[i - 1][0][2]

            else:
                dp[i][0][1] = dp[i - 1][0][1]
                dp[i][0][2] = dp[i - 1][0][2] + 1

result = 0
for i in range(w + 1):
    result = max(result, dp[t - 1][i][1], dp[t - 1][i][2])

print(result)
