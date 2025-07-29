import sys
input = sys.stdin.readline
INF = -10 ** 9


def dfs(cur, i, j):
    if (i, j) == (m, k):
        return 0

    if cur == n:
        return INF

    if dp[cur][i][j] != INF:
        return dp[cur][i][j]

    result = dp[cur][i][j]
    if i < m and j < k:
        result = max(result, arr1[i] * arr2[j] + dfs(cur + 1, i + 1, j + 1))

    if i < m:
        result = max(result, dfs(cur + 1, i + 1, j))

    if j < k:
        result = max(result, dfs(cur + 1, i, j + 1))

    dp[cur][i][j] = result
    return dp[cur][i][j]


n = int(input())
tmp1 = list(map(int, input().split()))
tmp2 = list(map(int, input().split()))

arr1, arr2 = [], []
for num in tmp1:
    if num:
        arr1.append(num)

for num in tmp2:
    if num:
        arr2.append(num)

m, k = map(len, [arr1, arr2])
dp = [[[INF] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

print(dfs(0, 0, 0))
