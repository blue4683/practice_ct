import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
INF = 10 ** 9


def dfs(now, before):
    if now == n:
        return 0

    if now > n or now in little:
        return INF

    result = dp[now][before]
    if result != -1:
        return result

    result = INF
    if before - 1 > 0:
        result = min(result, 1 + dfs(now + before - 1, before - 1))

    if before > 0:
        result = min(result, 1 + dfs(now + before, before))

    if before + 1 > 0:
        result = min(result, 1 + dfs(now + before + 1, before + 1))

    dp[now][before] = result
    return dp[now][before]


n, m = map(int, input().split())
little = set([int(input()) for _ in range(m)])
dp = [[-1] * (int((2 * n) ** 0.5) + 2) for _ in range(n + 1)]
result = dfs(1, 0)
print(result) if result != INF else print(-1)
