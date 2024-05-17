from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(start):
    result = [INF] * (n + 1)
    result[start] = 0
    heap = [[0, start]]
    while heap:
        now_cost, now = heappop(heap)
        if result[now] < now_cost:
            continue

        for next, next_cost in graph[now]:
            cost = now_cost + next_cost
            if result[next] > cost:
                result[next] = cost
                heappush(heap, [cost, next])

    return result


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    s_start = dijkstra(s)
    g_start = dijkstra(g)
    h_start = dijkstra(h)
    result = []
    for _ in range(t):
        x = int(input())

        case1 = s_start[g] + g_start[h] + h_start[x]
        case2 = s_start[h] + h_start[g] + g_start[x]

        if s_start[x] in [case1, case2]:
            result.append(x)

    print(*sorted(result))
