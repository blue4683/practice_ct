import sys
input = sys.stdin.readline
INF = 10 ** 9

n, k = map(int, input().split())
dp = [INF] * (10 ** 6 + 1)
for i in range(1, 4):
    dp[i] = i

for i in range(3, n + 1):
    if i + 1 <= n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    if i + i // 2 <= n:
        dp[i + i // 2] = min(dp[i + i // 2], dp[i] + 1)

if dp[n] > k:
    print('water')

else:
    print('minigimbob')
