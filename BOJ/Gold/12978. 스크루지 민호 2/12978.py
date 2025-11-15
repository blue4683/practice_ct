import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    for node in graph[now]:
        if visited[node]:
            continue

        visited[node] = 1
        no, yes = dfs(node)
        dp[now][0] += yes
        dp[now][1] += min(yes, no)

    return dp[now]


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)
visited[1] = 1
dp = [[0, 1] for _ in range(n + 1)]
print(min(dfs(1)))
