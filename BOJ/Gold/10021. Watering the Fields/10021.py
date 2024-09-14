from heapq import *
import sys
input = sys.stdin.readline


def bfs():
    connected = [0] * n
    heap = [(0, 0)]
    result = 0

    while heap:
        cost, now = heappop(heap)
        if connected[now]:
            continue

        connected[now] = 1
        result += cost
        y1, x1 = pipes[now]
        for i in range(n):
            if connected[i]:
                continue

            y2, x2 = pipes[i]
            field = (y2 - y1) ** 2 + (x2 - x1) ** 2
            if field < c:
                continue

            heappush(heap, (field, i))

    return result if connected == [1] * n else -1


n, c = map(int, input().split())
pipes = [tuple(map(int, input().split())) for _ in range(n)]

print(bfs())
