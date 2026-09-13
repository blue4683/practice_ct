from collections import deque


def bfs():
    q = deque([s])
    visited = [-1] * (n + 1)
    visited[s] = 0
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if visited[xx] != -1:
                continue
                
            visited[xx] = visited[x] + 1
            q.append(xx)

    return visited    


n, m, s = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
dists = bfs()
for i in range(1, n + 1):
    print(dists[i])
