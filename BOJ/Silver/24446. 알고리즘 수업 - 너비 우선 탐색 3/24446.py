from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [-1] * (n + 1)
    visited[r] = 0
    q = deque([r])
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if visited[xx] != -1:
                continue

            visited[xx] = visited[x] + 1
            q.append(xx)

    return visited


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = bfs()
for x in range(1, n + 1):
    print(visited[x])
