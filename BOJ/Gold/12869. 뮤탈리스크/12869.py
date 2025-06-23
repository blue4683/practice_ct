import sys
input = sys.stdin.readline
combs = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]


def dfs(a, b, c):
    if a < 0:
        return dfs(0, b, c)

    if b < 0:
        return dfs(a, 0, c)

    if c < 0:
        return dfs(a, b, 0)

    if (a, b, c) == (0, 0, 0):
        return 0

    if dp[a][b][c]:
        return dp[a][b][c]

    result = 10 ** 9
    for aa, bb, cc in combs:
        result = min(result, dfs(a - aa, b - bb, c - cc) + 1)

    dp[a][b][c] = result
    return dp[a][b][c]


n = int(input())
scvs = [0] * 3
for i, scv in enumerate(map(int, input().split())):
    scvs[i] = scv

a, b, c = scvs
dp = [[[0] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]
print(dfs(a, b, c))
