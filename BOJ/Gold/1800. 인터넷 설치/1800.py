from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    result = [[INF] * (n + 1) for _ in range(k + 1)]
    heap = []
    for i in range(k + 1):
        heappush(heap, (0, 1))
        while heap:
            now_cost, now = heappop(heap)
            if now_cost >= result[i][now]:
                continue

            result[i][now] = now_cost
            for next, next_cost in graph[now]:
                heappush(heap, (max(now_cost, next_cost), next))
                if not i:
                    continue

                heappush(heap, (result[i - 1][now], next))

    return result[k][n] if result[k][n] != INF else -1


n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(p):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

print(dijkstra())
