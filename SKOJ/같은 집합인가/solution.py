def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])
        
    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[y] = x
    
    else:
        graph[x] = y



n, m = map(int, input().split())
graph = [i for i in range(n + 1)]

for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        print('YES') if find(a) == find(b) else print('NO')
        
    else:
        union(a, b)
        