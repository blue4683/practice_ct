def find(x):
    root = x
    while graph[root] != root:
        root = graph[root]
        
    while graph[x] != root:
        graph[x], x = root, graph[x]
        
    return root


def union(x, y):
    x, y = find(x), find(y)
    if size[x] < size[y]:
        x, y = y, x
    
    connected = size[x] * size[y]    
    graph[y] = x
    size[x] += size[y]
    return connected


n, m = map(int, input().split())
graph = [i for i in range(n + 1)]
size = [1] * (n + 1)


result = (n * (n - 1)) // 2
for _ in range(m):
    a, b = map(int, input().split())        
    if find(a) != find(b):
        result -= union(a, b)
        
    print(result)
    