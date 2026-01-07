from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    heap = [(0, 1)]
    visited = [(INF, 0)] * (n + 1)
    visited[1] = (0, 0)
    while heap:
        cost, x = heappop(heap)
        if cost > visited[x][0]:
            continue

        for xx, c in graph[x]:
            if c + cost >= visited[xx][0]:
                continue

            visited[xx] = (c + cost, x)
            heappush(heap, (c + cost, xx))

    result = []
    for i in range(2, n + 1):
        if visited[i][0] != INF:
            result.append((i, visited[i][1]))

    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

result = dijkstra()
print(len(result))
for res in result:
    print(*res)
