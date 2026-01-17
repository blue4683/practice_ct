from collections import deque
import sys
input = sys.stdin.readline


def bfs(s, e):
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([s])
    while q:
        x = q.popleft()
        if x == e:
            return visited[x] - 1

        for node in graph[x]:
            if visited[node]:
                continue

            visited[node] = visited[x] + 1
            q.append(node)

    return -1


a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(a, b))
