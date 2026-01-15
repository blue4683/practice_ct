import sys
input = sys.stdin.readline


def dfs(x):
    global idx, result
    if visited[x] or not result:
        return

    visited[x] = 1
    is_leaf = 1
    tmp = idx
    for node in graph[x]:
        if visited[node]:
            continue

        is_leaf = 0
        if node == nodes[idx]:
            idx += 1
            dfs(node)

    if not is_leaf and tmp == idx:
        result = 0


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

nodes = tuple(map(int, input().split()))

result = 1
idx = 1
visited = [0] * (n + 1)
dfs(1)
print(result)
