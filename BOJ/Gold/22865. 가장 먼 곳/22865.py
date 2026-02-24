from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(s):
    heap = [(0, s)]
    dists = [INF] * (n + 1)
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


n = int(input())
a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))

dists = []
for i in [a, b, c]:
    dists.append(dijkstra(i))

result, dist = 0, 0
for i in range(1, n + 1):
    tmp = min(dists[j][i] for j in range(3))
    if tmp > dist:
        dist = tmp
        result = i

print(result)
