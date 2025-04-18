from heapq import *
import sys
input = sys.stdin.readline
INF = float('inf')


def dijkstra(max_cost):
    visited = [INF] * (n + 1)
    visited[a] = 0
    heap = [(0, a)]
    while heap:
        cost, node = heappop(heap)
        if cost > visited[node]:
            continue

        for next_node, next_cost in graph[node]:
            update_cost = cost + next_cost
            if next_cost > max_cost or update_cost > c or update_cost >= visited[next_node]:
                continue

            if next_node == b:
                return 1

            visited[next_node] = update_cost
            heappush(heap, (update_cost, next_node))

    return 0


n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
costs = set()
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    costs.add(w)

costs = sorted(list(costs))
result = -1
l, r = 0, len(costs) - 1
while l <= r:
    mid = (l + r) // 2
    if dijkstra(costs[mid]):
        result = costs[mid]
        r = mid - 1

    else:
        l = mid + 1

print(result)
