import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]

dp = [0] * 41
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

if m:
    before = 0
    result = 1
    for vip in vips:
        result *= dp[vip - 1 - before]
        before = vip

    print(result * dp[n - before])

else:
    print(dp[n])
