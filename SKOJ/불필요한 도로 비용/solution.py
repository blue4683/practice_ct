def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])
        
    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        graph[y] = x
        
    else:
        graph[x] = y
        

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[-1])

graph = [i for i in range(n + 1)]
result = sum([w for _, _, w in edges])
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        result -= w
        
print(result)
