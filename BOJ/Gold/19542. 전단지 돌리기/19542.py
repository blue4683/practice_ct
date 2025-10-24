import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(depth, now):
    global result
    max_dist = depth
    for node in graph[now]:
        if visited[node]:
            continue

        visited[node] = 1
        max_dist = max(max_dist, dfs(depth + 1, node))

    dist[now] = max_dist
    if now != s and dist[now] - depth >= d:
        result += 2

    return dist[now]


n, s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)
visited[s] = 1
dist = [0] * (n + 1)
result = 0

dfs(0, s)
print(result)
