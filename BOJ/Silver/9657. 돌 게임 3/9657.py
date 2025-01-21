n = int(input())
dp = [0] * 1001
for i in [1, 3, 4]:
    dp[i] = 1

for i in range(5, n + 1):
    if 0 in [dp[i - 1], dp[i - 3], dp[i - 4]]:
        dp[i] = 1

    else:
        dp[i] = 0

print('SK') if dp[n] else print('CY')
