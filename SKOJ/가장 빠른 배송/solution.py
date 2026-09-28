from heapq import heappop, heappush


def dijkstra():
    INF = float('inf')
    heap = [(0, 1)]
    dists = [INF] * (n + 1)
    dists[1] = 0
    while heap:
        dist, x = heappop(heap)
        if dists[x] > dist:
            continue
        
        for xx, cost in graph[x]:
            if dists[xx] <= dist + cost:
                continue
            
            dists[xx] = dist + cost
            heappush(heap, (dist + cost, xx))
            
    return dists[n] if dists[n] != INF else -1


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
print(dijkstra())
