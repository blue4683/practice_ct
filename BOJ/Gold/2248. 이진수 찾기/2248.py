import sys
input = sys.stdin.readline

n, l, i = map(int, input().split())
dp = [[0] * (l + 1) for _ in range(n + 1)]
dp[0][0] = 1
for j in range(1, n + 1):
    dp[j][0] = 1
    for k in range(1, l + 1):
        dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k]

result = ''
for j in range(n, 0, -1):
    cnt = sum(dp[j - 1][:l + 1])
    if cnt < i:
        result += '1'
        i -= cnt
        l -= 1

    else:
        result += '0'

print(result)
