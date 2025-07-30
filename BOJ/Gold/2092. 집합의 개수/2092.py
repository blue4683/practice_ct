import sys
input = sys.stdin.readline
MOD = 10 ** 6

t, a, s, b = map(int, input().split())
cnt = [0] * (t + 1)
for num in map(int, input().split()):
    cnt[num] += 1

dp = [[0] * (a + 1) for _ in range(t + 1)]
size = 0
for i in range(1, t + 1):
    if not cnt[i]:
        for j in range(size + 1):
            dp[i][j] = dp[i - 1][j]

    else:
        if not size:
            for j in range(cnt[i] + 1):
                dp[i][j] += 1
                dp[i][j] %= MOD

            size += cnt[i]

        else:
            for j in range(size + 1):
                for k in range(cnt[i] + 1):
                    dp[i][j + k] += dp[i - 1][j]
                    dp[i][j + k] %= MOD

            size += cnt[i]

print(sum(dp[t][s:b + 1]) % MOD)
