import sys

input = sys.stdin.readline

n, m = map(int, input().split())
apps = list(map(int, input().split()))
memories = list(map(int, input().split()))
dp = [[0] * (sum(memories) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    app, memory = apps[i - 1], memories[i - 1]

    for j in range(sum(memories) + 1):
        if j < memory:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(app + dp[i - 1][j - memory], dp[i - 1][j])

for i in range(sum(memories) + 1):
    if dp[n][i] >= m:
        print(i)
        break
