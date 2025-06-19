from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    heap = [(0, 0, 0, 0)]
    weight = [[INF] * 2 for _ in range(n + 1)]
    weight[0][0] = 0
    weight[0][1] = 0

    while heap:
        cost, w1, w2, now = heappop(heap)
        if now == 1:
            return cost

        if w1 > weight[now][0] and w2 > weight[now][1]:
            continue

        for node in range(n):
            if weight1[now][node] == '.':
                continue

            ww1 = w1 + int(weight1[now][node])
            ww2 = w2 + int(weight2[now][node])
            if weight[node][0] <= ww1 and weight[node][1] <= ww2:
                continue

            weight[node][0] = min(weight[node][0], ww1)
            weight[node][1] = min(weight[node][1], ww2)
            heappush(heap, (ww1 * ww2, ww1, ww2, node))

    return -1


n = int(input())
weight1 = [list(input().rstrip()) for _ in range(n)]
weight2 = [list(input().rstrip()) for _ in range(n)]
print(dijkstra())
