import sys
input = sys.stdin.readline

dp = [0] * 101
for i in range(1, 101):
    dp[i] = dp[i - 1] + 1
    if i >= 10:
        dp[i] = min(dp[i], dp[i - 10] + 1)

    if i >= 25:
        dp[i] = min(dp[i], dp[i - 25] + 1)

for _ in range(int(input())):
    n = int(input())
    result = 0
    while n:
        result += dp[n % 100]
        n //= 100

    print(result)
