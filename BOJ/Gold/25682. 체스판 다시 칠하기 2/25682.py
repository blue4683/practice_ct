import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        v = arr[i - 1][j - 1] != 'W' if (i +
                                         j) % 2 else arr[i - 1][j - 1] != 'B'
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + v

result = 10 ** 9
for i in range(k, n + 1):
    for j in range(k, m + 1):
        v = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
        result = min(result, v, k * k - v)

print(result)
