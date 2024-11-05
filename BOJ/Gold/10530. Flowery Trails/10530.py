from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(start, end):
    result = [INF] * p
    result[start] = 0
    heap = [(0, start)]
    while heap:
        dist, now = heappop(heap)
        if result[now] < dist:
            continue

        for peak, l in graph[now]:
            next_dist = dist + l
            if next_dist >= result[peak]:
                continue

            result[peak] = next_dist
            heappush(heap, (next_dist, peak))

    return result


p, t = map(int, input().split())
graph = [[] for _ in range(p)]

for _ in range(t):
    p1, p2, l = map(int, input().split())
    graph[p1].append((p2, l))
    graph[p2].append((p1, l))

dist1 = dijkstra(0, p - 1)
dist2 = dijkstra(p - 1, 0)

result = 0
for p1 in range(p):
    for p2, l in graph[p1]:
        if dist1[p1] + l + dist2[p2] == dist1[p - 1]:
            result += l

print(result * 2)
