import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    result = 0
    for node, dist in graph[now]:
        if visited[node]:
            continue

        visited[node] = 1
        result = max(result, dfs(node) + dist)

    return result


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [0] * (n + 1)
visited[1] = 1
print(dfs(1))
