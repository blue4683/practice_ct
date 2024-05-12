from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(start, end):
    result = [[INF, []] for _ in range(n + 1)]
    heap = []
    heappush(heap, [0, [start], start])

    while heap:
        now_cost, cities, now = heappop(heap)
        if result[now][0] < now_cost:
            continue

        for next, next_cost in graph[now]:
            cost = now_cost + next_cost
            if cost < result[next][0]:
                result[next] = [cost, cities + [next]]
                heappush(heap, [cost, cities + [next], next])

    return result[end]


n, m = [int(input()) for _ in range(2)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

s, e = map(int, input().split())
cost, cities = dijkstra(s, e)
print(cost)
print(len(cities))
print(*cities)
