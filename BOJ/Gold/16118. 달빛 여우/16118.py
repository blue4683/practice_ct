from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(is_wolf):
    dist = [[INF] * 2 for _ in range(n + 1)]
    dist[1][0] = 0
    heap = [(0, 1, 0)]
    while heap:
        c, x, run = heappop(heap)
        if c > dist[x][run]:
            continue

        for xx, cost in graph[x]:
            if is_wolf:
                cc = c + cost * 2 if run else c + cost / 2

            else:
                cc = c + cost

            if is_wolf and cc < dist[xx][run ^ 1]:
                dist[xx][run ^ 1] = cc
                heappush(heap, (cc, xx, run ^ 1))

            elif not is_wolf and cc < dist[xx][0]:
                dist[xx][0] = cc
                heappush(heap, (cc, xx, 0))

    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

fox, wolf = dijkstra(0), dijkstra(1)
result = 0
for i in range(2, n + 1):
    result += int(fox[i][0] < min(wolf[i]))

print(result)
