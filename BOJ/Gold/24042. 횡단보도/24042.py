from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 12


def dijkstra():
    heap = [(0, 1)]
    while heap:
        now_cost, now = heappop(heap)
        if result[now] < now_cost:
            continue

        for next, next_cost in graph[now]:
            cost = next_cost - now_cost % m
            if cost < 0:
                cost += m

            cost += now_cost
            if cost < result[next]:
                result[next] = cost
                heappush(heap, (result[next], next))

    return result[n]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

result = [INF] * (n + 1)
result[1] = 0
print(dijkstra())
