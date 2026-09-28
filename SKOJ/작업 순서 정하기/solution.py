n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort()

indegree = [0] * (n + 1)
for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1

result = []
q = []
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
        
while q:
    q.sort(reverse=True)
    x = q.pop()
    result.append(x)
    for xx in graph[x]:
        indegree[xx] -= 1
        if not indegree[xx]:
            q.append(xx)
            
print(*result)
