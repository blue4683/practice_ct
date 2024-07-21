from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    heap = [(0, 1)]
    while heap:
        now_cost, now = heappop(heap)
        if result[now] < now_cost:
            continue

        for next, next_cost in graph[now]:
            cost = now_cost + next_cost
            if cost < result[next]:
                result[next] = cost
                heappush(heap, (cost, next))

    return result[n]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

result = [INF] * (n + 1)
print(dijkstra())
