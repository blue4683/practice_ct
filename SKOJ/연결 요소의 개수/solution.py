def dfs(x): 
    for xx in graph[x]:
        if visited[xx]:
            continue
        
        visited[xx] = 1
        dfs(xx)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
visited = [0] * (n + 1)
for i in range(1, n + 1):
    if visited[i]:
        continue

    visited[i] = 1
    result += 1
    dfs(i)
    
print(result)
