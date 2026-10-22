def bfs(sx):
    visited = [-1] * (n + 1)
    dist, node = -1, -1
    q = [sx]
    visited[sx] = 0
    while q:
        x = q.pop()
        if visited[x] > dist:
            dist, node = visited[x], x
            
        for xx in graph[x]:
            if visited[xx] != -1:
                continue
            
            visited[xx] = visited[x] + 1
            q.append(xx)
            
    return node, visited[node]


n = int(input())
if n == 1:
    print(0)
    
else:
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    x, _ = bfs(1)
    _, result = bfs(x)
    print(result)
    