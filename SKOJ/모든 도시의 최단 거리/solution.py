n, m = map(int, input().split())
INF = float('inf')

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)

for i in range(1, n + 1):
    graph[i][i] = 0

for mid in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if graph[s][e] > graph[s][mid] + graph[mid][e]:
                graph[s][e] = graph[s][mid] + graph[mid][e]
                
for i in range(1, n + 1):
    print(*map(lambda x: x if x != INF else 0, graph[i][1:]))
    