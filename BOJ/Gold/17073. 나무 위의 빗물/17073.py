from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1
    leaf_nodes = 0
    while q:
        x = q.popleft()
        leaf = 1
        for xx in graph[x]:
            if visited[xx]:
                continue

            leaf = 0
            visited[xx] = 1
            q.append(xx)

        if leaf:
            leaf_nodes += 1

    return w / leaf_nodes


n, w = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs())
