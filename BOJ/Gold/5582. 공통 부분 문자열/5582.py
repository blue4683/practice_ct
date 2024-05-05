import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
n, m = map(len, [s, t])
dp = [[0] * (m + 1) for _ in range(n + 1)]
result = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])

print(result)
