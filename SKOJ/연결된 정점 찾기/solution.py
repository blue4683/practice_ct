def dfs(x):
    print(x, end=' ')
    for xx in graph[x]:
        if visited[xx]:
            continue
        
        visited[xx] = 1
        dfs(xx)


n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, n + 1):
    graph[i].sort()
    
visited = [0] * (n + 1)
visited[s] = 1
dfs(s)
