from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dfs(x, visit):
    global result
    if result:
        return

    if x == v:
        if visit:
            result = 1

        return

    for node, cost in graph[x]:
        if dist[node] != dist[x] + cost:
            continue

        dfs(node, visit | (node == p))


def dijkstra():
    dist = [INF] * (v + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        c, x = heappop(heap)
        if c > dist[x]:
            continue

        for node, cost in graph[x]:
            if c + cost >= dist[node]:
                continue

            dist[node] = c + cost
            heappush(heap, (c + cost, node))

    return dist


v, e, p = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = dijkstra()

result = 0
dfs(1, 1 == p)
print('SAVE HIM') if result else print('GOOD BYE')
