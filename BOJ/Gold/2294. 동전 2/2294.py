import sys
input = sys.stdin.readline
INF = 10 ** 9

n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))

dp = [INF] * (k + 1)
dp[0] = 0
for i in range(1, k + 1):
    for coin in coins:
        if i - coin < 0:
            continue

        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k]) if dp[k] != INF else print(-1)
