import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
    exit()

dp = [[-10 ** 9] * 2 for _ in range(n)]
dp[0][0] = arr[0]

for i in range(1, n):
    dp[i][0] = max(arr[i], dp[i - 1][0] + arr[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])

print(max(map(max, dp)))
