n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
    
for l in graph:
    print(*l)
    