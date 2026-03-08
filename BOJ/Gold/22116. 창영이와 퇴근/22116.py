from heapq import *
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 10 ** 9


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs():
    heap = [(0, 0, 0)]
    visited = [[INF] * n for _ in range(n)]
    visited[0][0] = 0
    while heap:
        h, y, x = heappop(heap)
        if h > visited[y][x]:
            continue

        if (y, x) == (n - 1, n - 1):
            return h

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] <= max(h, abs(arr[yy][xx] - arr[y][x])):
                continue

            visited[yy][xx] = max(h, abs(arr[yy][xx] - arr[y][x]))
            heappush(heap, (visited[yy][xx], yy, xx))

    return INF


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(bfs())
