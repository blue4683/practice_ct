from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    dists = [INF] * n
    dists[y] = 0
    heap = [(0, y)]
    while heap:
        d, x = heappop(heap)
        if d > dists[x]:
            continue

        for xx, dd in graph[x]:
            if d + dd >= dists[xx]:
                continue

            dists[xx] = d + dd
            heappush(heap, (d + dd, xx))

    return sorted([(dists[i], i) for i in range(n) if i != y])


n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dists = dijkstra()
result = 0
remain = x
for dist, i in dists:
    if dist * 2 > x:
        result = -1
        break

    if dist * 2 > remain:
        result += 1
        remain = x

    remain -= dist * 2

else:
    result += 1

print(result)
