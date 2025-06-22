import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n)]
dp[0][arr[0]] = 1

for j in range(1, n - 1):
    for i in range(21):
        if not dp[j - 1][i]:
            continue

        if i + arr[j] <= 20:
            dp[j][i + arr[j]] += dp[j - 1][i]

        if i - arr[j] >= 0:
            dp[j][i - arr[j]] += dp[j - 1][i]

print(dp[n - 2][arr[n - 1]])
