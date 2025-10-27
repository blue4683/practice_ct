import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now, rd, ld):
    global dist, max_dist
    if (now == r and len(graph[now]) > 1 or len(graph[now]) > 2) and dist == -1:
        dist = rd

    leaf = 1
    for node, d in graph[now]:
        if visited[node]:
            continue

        leaf = 0
        visited[node] = 1
        if dist != -1:
            dfs(node, rd, ld + d)

        else:
            dfs(node, rd + d, ld)

    if leaf:
        max_dist = max(max_dist, ld)
        if dist == -1:
            dist = rd


n, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

dist, max_dist = -1, 0
visited = [0] * (n + 1)
visited[r] = 1
dfs(r, 0, 0)

if dist == -1:
    dist = max_dist

print(dist, max_dist)
