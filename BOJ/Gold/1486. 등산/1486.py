from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def get_height(x):
    if ord(x) >= ord('a'):
        return ord(x) - ord('A') - 6

    return ord(x) - ord('A')


def get_node(y, x):
    return y * m + x


def dijkstra(graph):
    heap = [(0, 0)]
    dists = [INF] * (n * m)
    dists[0] = 0
    while heap:
        w, x = heappop(heap)
        if w > dists[x]:
            continue

        for xx, ww in graph[x]:
            if dists[xx] <= w + ww or w + ww > d:
                continue

            dists[xx] = w + ww
            heappush(heap, (w + ww, xx))

    return dists


n, m, t, d = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
graph = [[] for _ in range(n * m)]
reverse_graph = [[] for _ in range(n * m)]
for y in range(n):
    for x in range(m):
        for dy, dx in direction:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            a, b = get_node(y, x), get_node(yy, xx)
            h, hh = get_height(arr[y][x]), get_height(arr[yy][xx])
            if abs(hh - h) > t:
                continue

            w = 1 if h >= hh else (hh - h) ** 2
            graph[a].append((b, w))
            reverse_graph[b].append((a, w))

dists = dijkstra(graph)
reverse_dists = dijkstra(reverse_graph)

result = 0
for y in range(n):
    for x in range(m):
        i = get_node(y, x)
        if dists[i] + reverse_dists[i] > d or get_height(arr[y][x]) <= result:
            continue

        result = get_height(arr[y][x])

print(result)
