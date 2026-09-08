from heapq import heappop, heappush
import math
INF = math.inf


def dijkstra():
    heap = [(0, s, 1)]
    dists = [[INF, INF] for _ in range(n + 1)]
    dists[s][0] = 0
    while heap:
        dist, now, discount = heappop(heap)
        if dists[now][discount ^ 1] < dist:
            continue

        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < dists[next_node][discount ^ 1]:
                dists[next_node][discount ^ 1] = cost
                heappush(heap, (cost, next_node, discount))
            
            if discount:
                cost = dist + next_dist // 2
                if cost < dists[next_node][1]:
                    dists[next_node][1] = cost
                    heappush(heap, (cost, next_node, 0))
                
    return min(dists[t]) if min(dists[t]) != INF else -1

n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

print(dijkstra())
