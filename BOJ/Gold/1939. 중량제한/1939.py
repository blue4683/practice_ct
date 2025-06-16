from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    result = [0] * (n + 1)
    result[s] = INF
    heap = [(-INF, s)]
    while heap:
        weight, now = heappop(heap)
        if -weight < result[now]:
            continue

        for node, limit in graph[now]:
            if result[node] >= min(limit, result[now]):
                continue

            result[node] = min(limit, result[now])
            heappush(heap, (-result[node], node))

    return result[e]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, e = map(int, input().split())
print(dijkstra())
