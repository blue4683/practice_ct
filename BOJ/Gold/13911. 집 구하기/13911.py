from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(pos, bound):
    heap = [(0, p) for p in pos]
    dists = [INF] * (v + 1)
    for p in pos:
        dists[p] = 0

    while heap:
        d, node = heappop(heap)
        if d > dists[node]:
            continue

        for dist, next_node in graph[node]:
            if d + dist >= dists[next_node] or d + dist > bound:
                continue

            dists[next_node] = d + dist
            heappush(heap, (d + dist, next_node))

    return {i for i in range(1, v + 1) if dists[i] <= bound}, dists


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, v + 1):
    graph[i].sort()

m, x = map(int, input().split())
xpos = set(map(int, input().split()))
s, y = map(int, input().split())
ypos = set(map(int, input().split()))

xpossible, xdist = dijkstra(xpos, x)
ypossible, ydist = dijkstra(ypos, y)

pos = (xpossible & ypossible) - (xpos | ypos)
result = INF
for p in pos:
    result = min(result, xdist[p] + ydist[p])

print(result) if result != INF else print(-1)
