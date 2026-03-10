from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(s):
    heap = [(0, s)]
    dists = [INF] * (n + 1)
    dists[s] = 0
    while heap:
        dist, x = heappop(heap)
        if dist > dists[x]:
            continue

        for xx, c in graph[x]:
            if c + dist >= dists[xx] or h[x] >= h[xx]:
                continue

            dists[xx] = c + dist
            heappush(heap, (c + dist, xx))

    return dists


n, m, d, e = map(int, input().split())
h = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dists_a = dijkstra(1)
dists_b = dijkstra(n)
result = -INF

for i in range(2, n):
    if INF in {dists_a[i], dists_b[i]}:
        continue

    result = max(result, h[i] * e - (dists_a[i] + dists_b[i]) * d)

print(result if result != -INF else 'Impossible')
