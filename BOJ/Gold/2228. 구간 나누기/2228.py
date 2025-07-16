import sys
input = sys.stdin.readline


def dfs(k, depth):
    if k == m:
        return 0

    if depth >= n:
        return -10 ** 9

    if dp[k][depth] != -1:
        return dp[k][depth]

    dp[k][depth] = dfs(k, depth + 1)
    tmp = 0
    for i in range(depth, n):
        tmp += arr[i]
        ret = dfs(k + 1, i + 2) + tmp
        if ret > dp[k][depth]:
            dp[k][depth] = ret

    return dp[k][depth]


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [[-1] * n for _ in range(m + 1)]
print(dfs(0, 0))
