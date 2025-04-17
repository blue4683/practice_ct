from heapq import *
import sys
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    result = [INF] * (n + 1)
    heap = []
    for dest in dests:
        result[dest] = 0
        heappush(heap, (0, dest))

    while heap:
        c, x = heappop(heap)
        if c > result[x]:
            continue

        for xx, cc in graph[x]:
            if c + cc >= result[xx]:
                continue

            result[xx] = c + cc
            heappush(heap, (c + cc, xx))

    return result


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v].append((u, c))

dests = list(map(int, input().split()))
result = dijkstra()

num, cost = 0, 0
for i in range(1, n + 1):
    if result[i] != INF and result[i] > cost:
        num, cost = i, result[i]

print(num)
print(cost)
