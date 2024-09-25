from heapq import *
from itertools import permutations
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(start):
    market = markets[start]
    heap = [(0, market)]
    while heap:
        now_cost, node = heappop(heap)
        if now_cost >= result:
            break

        if distances[start][node] != INF:
            continue

        if node != market:
            distances[start][node] = now_cost

        for next_node, next_cost in graph[node]:
            cost = now_cost + next_cost
            if distances[start][next_node] != INF:
                continue

            heappush(heap, (cost, next_node))


n, m, k = map(int, input().split())
markets = [int(input()) for _ in range(k)]
distances = [[INF] * (n + 1) for _ in range(k)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j, l = map(int, input().split())
    graph[i].append((j, l))
    graph[j].append((i, l))

result = INF
for i in range(k):
    dijkstra(i)

for order in permutations(range(k)):
    cost = 0
    for i in range(k - 1):
        cost += distances[order[i]][markets[order[i + 1]]]

    for node in range(1, n + 1):
        if node in markets:
            continue

        result = min(result, cost +
                     distances[order[k - 1]][node] + distances[order[0]][node])

print(result)
