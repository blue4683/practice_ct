from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def trace(now, check):
    if now == n:
        paths.append(check)
        return

    for node, dist in graph[now]:
        if dists[now] + dist != dists[node]:
            continue

        trace(node, check + [node])


def dijkstra(a=0, b=0):
    heap = [(0, 1)]
    dists = [INF] * (n + 1)
    dists[1] = 0
    while heap:
        c, x = heappop(heap)
        if c > dists[x]:
            continue

        for xx, cc in graph[x]:
            if (a, b) in {(x, xx), (xx, x)} or c + cc >= dists[xx]:
                continue

            dists[xx] = c + cc
            heappush(heap, (c + cc, xx))

    return dists


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

dists = dijkstra()
result = -1
paths = []
trace(1, [1])

result = 0
for path in paths:
    for i in range(len(path) - 1):
        dist = dijkstra(path[i], path[i + 1])
        if dist[n] == INF:
            print(-1)
            exit()

        result = max(result, dist[n] - dists[n])

print(result)
