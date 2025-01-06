import sys
input = sys.stdin.readline

n = int(input())
counsels = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    time, cost = counsels[i]
    if i + time > n:
        dp[i] = dp[i + 1]

    else:
        dp[i] = max(dp[i + 1], dp[i + time] + cost)

print(dp[0])
