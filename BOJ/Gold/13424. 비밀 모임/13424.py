from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(s):
    heap = [(0, s)]
    dist = [INF] * (n + 1)
    dist[s] = 0
    while heap:
        c, x = heappop(heap)
        if c > dist[x]:
            continue

        for xx, cost in graph[x]:
            if cost + c >= dist[xx]:
                continue

            dist[xx] = cost + c
            heappush(heap, (cost + c, xx))

    return dist


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    k = int(input())
    arr = list(map(int, input().split()))
    dists = [dijkstra(i) for i in arr]
    num, dist = 0, INF
    for i in range(1, n + 1):
        tmp = 0
        for j in range(k):
            tmp += dists[j][i]

        if tmp < dist:
            num, dist = i, tmp

    print(num)
