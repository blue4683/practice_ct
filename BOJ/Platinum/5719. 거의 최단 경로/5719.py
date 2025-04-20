from collections import deque
from heapq import *
import sys
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        c, x = heappop(heap)
        if c > dist[x]:
            continue

        for xx, cc in graph[x]:
            if c + cc >= dist[xx] or dropped[x][xx]:
                continue

            dist[xx] = c + cc
            heappush(heap, (c + cc, xx))

    return


def bfs():
    q = deque([d])
    while q:
        x = q.popleft()
        if x == s:
            continue

        for xx, c in reverse_graph[x]:
            if dropped[xx][x] or dist[x] != dist[xx] + c:
                continue

            dropped[xx][x] = 1
            q.append(xx)


while 1:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    s, d = map(int, input().split())
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        reverse_graph[v].append((u, p))

    dist = [INF] * n
    dropped = [[0] * n for _ in range(n)]
    dijkstra()
    bfs()

    dist = [INF] * n
    dijkstra()
    print(dist[d] if dist[d] != INF else -1)
