import sys
input = sys.stdin.readline


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
for i in range(3):
    dp[0][i] = arr[0][i]

result = []
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][:2]) + arr[i][0]
    dp[i][1] = max(dp[i - 1]) + arr[i][1]
    dp[i][2] = max(dp[i - 1][1:]) + arr[i][2]

result.append(max(dp[-1]))
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][:2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][1:]) + arr[i][2]

result.append(min(dp[-1]))
print(*result)
