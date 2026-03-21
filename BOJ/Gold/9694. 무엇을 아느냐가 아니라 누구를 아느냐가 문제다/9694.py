from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    heap = [(0, 0)]
    visited = [INF] * m
    visited[0] = 0
    parent = [-1] * m
    while heap:
        z, x = heappop(heap)
        if z > visited[x]:
            continue

        for xx, zz in graph[x]:
            if z + zz >= visited[xx]:
                continue

            parent[xx] = x
            visited[xx] = z + zz
            heappush(heap, (z + zz, xx))

    result = []
    cur = m - 1
    while cur:
        if cur == -1:
            return [-1]

        result.append(cur)
        cur = parent[cur]

    result.append(0)
    result.reverse()
    return result


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(m)]
    for _ in range(n):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))
        graph[y].append((x, z))

    result = dijkstra()
    print(f'Case #{t}:', *result)
