def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])
        
    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if size[x] < size[y]:
        x, y = y, x
        
    graph[y] = x
    size[x] += size[y]


n, q = map(int, input().split())
graph = [i for i in range(n + 1)]
size = [1] * (n + 1)

for _ in range(q):
    command, *args = map(int, input().split())
    if command == 1:
        x, y = args
        if find(x) != find(y):
            union(x, y)
            
    elif command == 2:
        x, y = args
        print('YES') if find(x) == find(y) else print('NO')
        
    else:
        x = args[0]
        print(size[find(x)])
        