import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    for node in graph[now]:
        if visited[node] != -1:
            continue

        visited[node] = visited[now] + 1
        dfs(node)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

visited = [-1] * (n + 1)
visited[r] = 0
dfs(r)

for i in range(1, n + 1):
    print(visited[i])
