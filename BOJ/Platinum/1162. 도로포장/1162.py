from heapq import *
import sys
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    result = [[INF] * (n + 1) for _ in range(k + 1)]
    result[0][1] = 0
    heap = [(0, 0, 1)]
    while heap:
        c, p, x = heappop(heap)
        if c > result[p][x]:
            continue

        for xx, cc in graph[x]:
            if p < k and result[p + 1][xx] > c:
                result[p + 1][xx] = c
                heappush(heap, (c, p + 1, xx))

            if c + cc >= result[p][xx]:
                continue

            result[p][xx] = c + cc
            heappush(heap, (c + cc, p, xx))

    return min([result[i][n] for i in range(k + 1)])


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

print(dijkstra())
