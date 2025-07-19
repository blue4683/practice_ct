import sys
input = sys.stdin.readline


def dfs(depth, now):
    if now == n:
        return 0

    if depth == m:
        return -10 ** 9

    if dp[now][depth] != -10 ** 9:
        return dp[now][depth]

    for node in range(now + 1, n + 1):
        if not graph[now][node]:
            continue

        dp[now][depth] = max(dp[now][depth], dfs(
            depth + 1, node) + graph[now][node])

    return dp[now][depth]


n, m, k = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    if a > b:
        continue

    graph[a][b] = max(graph[a][b], c)

dp = [[-10 ** 9] * (m + 1) for _ in range(n + 1)]
print(dfs(1, 1))
