n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for mid in range(n):
    for s in range(n):
        if not graph[s][mid]:
            continue
        
        for e in range(n):
            if not graph[s][e] and graph[s][mid] and graph[mid][e]:
                graph[s][e] = 1
                
for i in range(n):
    print(*graph[i])    
