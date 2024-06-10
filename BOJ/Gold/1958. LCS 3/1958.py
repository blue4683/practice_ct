import sys
input = sys.stdin.readline

words = [input().rstrip() for _ in range(3)]
n, m, o = map(len, words)
dp = [[[0] * (o + 1) for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        for k in range(o + 1):
            if 0 in (i, j, k):
                dp[i][j][k] = 0

            elif len(set([words[0][i - 1], words[1][j - 1], words[2][k - 1]])) == 1:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1

            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i]
                                  [j - 1][k], dp[i][j][k - 1])

print(dp[i][j][k])
