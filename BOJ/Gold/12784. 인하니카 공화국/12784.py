import sys
input = sys.stdin.readline
INF = 10 ** 9


def dfs(now):
    if dp[now] != INF:
        return dp[now]

    cost = 0
    for node, c in graph[now]:
        if visited[node]:
            dp[now] = min(dp[now], c)
            continue

        visited[node] = 1
        cost += dfs(node)

    if cost:
        dp[now] = min(cost, dp[now])

    return dp[now]


for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
        continue

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))

    dp = [INF] * (n + 1)
    visited = [0] * (n + 1)
    visited[1] = 1
    print(dfs(1))
