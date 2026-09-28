from heapq import heappop, heappush
INF = float('inf')


def dijkstra():
    heap = [(0, s)]
    dists = [INF] * (n + 1)
    dists[s] = 0
    while heap:
        dist, x = heappop(heap)
        if dists[x] > dist:
            continue
        
        for xx, cost in graph[x]:
            if dists[xx] <= dist + cost:
                continue
            
            dists[xx] = dist + cost
            heappush(heap, (dist + cost, xx))
            
    return dists


n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
dists = dijkstra()
for i in range(1, n + 1):
    print(dists[i]) if dists[i] != INF else print(-1)
    