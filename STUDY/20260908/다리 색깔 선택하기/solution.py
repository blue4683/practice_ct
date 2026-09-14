import math
INF = math.inf

def find(x):
    if graph[x] != x:
        graph[x] = find(graph[x])
        
    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x <= y:
        graph[y] = x
    
    else:
        graph[x] = y
        

k, p = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(28)]
edges.sort(key=lambda x: x[2])
result = INF

for bit in range(1 << k):
    if bin(bit).count("1") != p:
        continue

    graph = [i for i in range(9)]
    cost = []
    for u, v, w, c in edges:
        if len(cost) == 7:
            break
        
        if bit & (1 << (c - 1)) and find(u) != find(v):
            union(u, v)
            cost.append(w)

    if len(cost) != 7:
        continue

    result = min(result, sum(cost))

print(result if result != INF else -1)
