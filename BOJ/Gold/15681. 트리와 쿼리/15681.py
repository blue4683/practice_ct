import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    if visited[now]:
        return dp[now]

    visited[now] = 1
    for next in graph[now]:
        if visited[next]:
            continue

        dp[now] += dfs(next)

    return dp[now]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [1] * (n + 1)
visited = [0] * (n + 1)
dfs(r)

for _ in range(q):
    print(dp[int(input())])
