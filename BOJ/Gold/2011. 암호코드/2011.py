import sys
input = sys.stdin.readline

password = ' ' + input().rstrip()
if password[1] == '0':
    print(0)
    exit()

n = len(password)
dp = [0] * n
dp[0] = 1
dp[1] = 1
for i in range(2, n):
    if int(password[i]):
        dp[i] += dp[i - 1]

    if 10 <= int(password[i - 1] + password[i]) <= 26:
        dp[i] += dp[i - 2]


print(dp[n - 1] % 1000000)
