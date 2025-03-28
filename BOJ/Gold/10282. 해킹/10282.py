from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    heap = [(0, c)]
    visited = [INF] * (n + 1)
    visited[c] = 0
    while heap:
        t, x = heappop(heap)
        if visited[x] < t:
            continue

        for xx, tt in graph[x]:
            if t + tt >= visited[xx]:
                continue

            visited[xx] = t + tt
            heappush(heap, (t + tt, xx))

    cnt = 0
    result = 0
    for v in visited:
        if v == INF:
            continue

        result = max(result, v)
        cnt += 1

    print(cnt, result)
