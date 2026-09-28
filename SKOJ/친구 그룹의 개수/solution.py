def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])
        
    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y
        
    else:
        graph[y] = x


n, m = map(int, input().split())
graph = [i for i in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    if find(u) != find(v):
        union(u, v)
        
for i in range(1, n + 1):
    find(i)

print(len(set(graph)) - 1)
