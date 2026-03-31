from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dfs(x):
    if x == 2:
        return 1

    if dp[x] != -1:
        return dp[x]

    dp[x] = 0
    for xx, _ in graph[x]:
        if dists[xx] < dists[x]:
            dp[x] += dfs(xx)

    return dp[x]


def dijkstra(s):
    heap = [(0, s)]
    dists = [INF] * (n + 1)
    dists[s] = 0
    while heap:
        d, x = heappop(heap)
        if d > dists[x]:
            continue

        for xx, dist in graph[x]:
            if d + dist >= dists[xx]:
                continue

            dists[xx] = d + dist
            heappush(heap, (d + dist, xx))

    return dists


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dists = dijkstra(2)
dp = [-1] * (n + 1)

print(dfs(1))
