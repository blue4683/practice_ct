from heapq import *
import sys
input = sys.stdin.readline


def topology_sort():
    result = []
    heap = []

    for i in range(1, n + 1):
        if not indegree[i]:
            heappush(heap, i)

    while heap:
        now = heappop(heap)
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if not indegree[next]:
                heappush(heap, next)

    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = topology_sort()
print(*result)
