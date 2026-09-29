INF = float('inf')
n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0
    
for _ in range(m):
    u, v, w = map(int, input().split())
    if graph[u - 1][v - 1] > w:
        graph[u - 1][v - 1] = w
    
for mid in range(n):
    for s in range(n):
        if graph[s][mid] == INF:
            continue
        
        for e in range(n):
            if graph[s][e] > graph[s][mid] + graph[mid][e]:
                graph[s][e] = graph[s][mid] + graph[mid][e]
                
for i in range(n):
    print(*map(lambda x: x if x != INF else -1, graph[i]))
