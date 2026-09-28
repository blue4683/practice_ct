from heapq import heappop, heappush


def dijkstra():
    INF = float('inf')
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
            
    return dists[t] if dists[t] != INF else -1


n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
print(dijkstra())
