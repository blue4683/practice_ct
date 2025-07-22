import sys
input = sys.stdin.readline


def is_koi(l, r):
    if (dna[l], dna[r]) in [('a', 't'), ('g', 'c')]:
        return 1

    return 0


dna = input().rstrip()
n = len(dna)
dp = [[0] * n for _ in range(n)]

for i in range(n - 1):
    if is_koi(i, i + 1):
        dp[i][i + 1] = 2

for i in range(n - 2):
    if dp[i][i + 1] or dp[i + 1][i + 2] or is_koi(i, i + 2):
        dp[i][i + 2] = 2

for k in range(3, n):
    for i in range(n - k):
        dp[i][i + k] = dp[i + 1][i + k - 1] + 2 * is_koi(i, i + k)
        for j in range(k):
            tmp = dp[i][i + j] + dp[i + j + 1][i + k]
            if tmp > dp[i][i + k]:
                dp[i][i + k] = tmp

print(dp[0][n - 1])
