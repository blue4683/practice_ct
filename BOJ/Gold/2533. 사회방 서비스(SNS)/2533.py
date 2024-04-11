import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    visited[now] = 1
    dp[now][0] = 1
    for next in graph[now]:
        if visited[next]:
            continue

        dfs(next)
        dp[now][1] += dp[next][0]
        dp[now][0] += min(dp[next][1], dp[next][0])


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0] * 2 for _ in range(n + 1)]
visited = [0] * (n + 1)
dfs(1)

print(min(dp[1]))
