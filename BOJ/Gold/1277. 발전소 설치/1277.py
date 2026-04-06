from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 10 ** 9


def get_dist(x, y):
    x1, y1 = pos[x - 1]
    x2, y2 = pos[y - 1]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def dijkstra():
    heap = [(0, 1)]
    dists = [INF] * (n + 1)
    dists[1] = 0
    while heap:
        d, x = heappop(heap)
        if d > dists[x]:
            continue

        for xx in range(1, n + 1):
            if x == xx:
                continue

            dd = 0 if xx in graph[x] else get_dist(x, xx)
            if dd > m or d + dd >= dists[xx]:
                continue

            dists[xx] = d + dd
            heappush(heap, (d + dd, xx))

    return int((dists[n] * 1000) // 1)


n, w = map(int, input().split())
m = float(input())
pos = [tuple(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n + 1)]
for _ in range(w):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dijkstra())
