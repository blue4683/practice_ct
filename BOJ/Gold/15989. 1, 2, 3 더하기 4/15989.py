import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]
n = max(arr)
dp = [1] * (n + 1)

for i in range(2, n + 1):
    dp[i] += dp[i - 2]

for i in range(3, n + 1):
    dp[i] += dp[i - 3]

for num in arr:
    print(dp[num])
