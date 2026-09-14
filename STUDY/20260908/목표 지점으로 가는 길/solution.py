def bfs():
    q = [t]
    while q:
        x = q.pop()
        for nx in graph[x]:
            if nx in visited:
                continue
            
            visited.add(nx)
            q.append(nx)
            
    return len(visited)


n, m, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    
visited = {t}
print(bfs())
print(*sorted(visited))
