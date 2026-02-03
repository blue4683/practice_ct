from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def swap(x, l, r):
    x = list(x)
    x[l], x[r] = x[r], x[l]
    return tuple(x)


def dijkstra():
    visited = defaultdict(lambda: INF)
    s = tuple(arr)
    visited[s] = 0
    heap = [(0, s)]
    while heap:
        c, x = heappop(heap)
        for c, l, r in costs:
            xx = swap(x, l, r)
            if visited[x] + c >= visited[xx]:
                continue

            visited[xx] = visited[x] + c
            heappush(heap, (visited[x] + c, xx))

    return visited


n = int(input())
arr = list(map(int, input().split()))

costs = []
m = int(input())
for _ in range(m):
    l, r, c = map(int, input().split())
    costs.append((c, l - 1, r - 1))

costs.sort()
result = dijkstra()
sorted_arr = tuple(sorted(arr))
print(result[sorted_arr]) if result[sorted_arr] != INF else print(-1)
