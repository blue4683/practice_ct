from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 10 ** 9


def get_dist(d):
    return -1 if d == INF else d


def dijkstra(s):
    heap = [(0, s)]
    dists = [INF] * (v + 1)
    dists[s] = 0
    while heap:
        d, x = heappop(heap)
        if d > dists[x]:
            continue

        for xx, dd in graph[x]:
            if d + dd >= dists[xx]:
                continue

            dists[xx] = d + dd
            heappush(heap, (d + dd, xx))

    return dists


n, v, e = map(int, input().split())
start, end = map(int, input().split())
h = list(map(int, input().split()))

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

dists = [dijkstra(i) for i in [start, end]]
result = 0
for i in h:
    d1, d2 = get_dist(dists[0][i]), get_dist(dists[1][i])
    result += d1 + d2

print(result)
