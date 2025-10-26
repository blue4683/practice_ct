from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 12


def dijkstra():
    heap = [(0, 0)]
    result = [INF] * n
    while heap:
        cost, now = heappop(heap)
        if cost > result[now]:
            continue

        for node, c in graph[now]:
            if cost + c >= result[node] or (node != n - 1 and arr[node]):
                continue

            result[node] = cost + c
            heappush(heap, (cost + c, node))

    return result[n - 1] if result[n - 1] != INF else -1


n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

print(dijkstra())
