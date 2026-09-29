n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for mid in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if not graph[s][e] and graph[s][mid] and graph[mid][e]:
                graph[s][e] = 1
                
for i in range(1, n + 1):
    print(*graph[i][1:])    
