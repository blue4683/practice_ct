import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = [0] * (2 * (10 ** 7) + 1)
max_h = 0
for _ in range(n):
    h, c = map(int, input().split())
    max_h = max(max_h, h)
    arr[h] = max(arr[h], c)

dp = [0] * (2 * (10 ** 7) + 1)
for i in range(s + 1):
    dp[i] = arr[i]

for i in range(s + 1, max_h + 1):
    dp[i] = dp[i - 1]
    dp[i] = max(dp[i], dp[i - s] + arr[i])

print(dp[max_h])
