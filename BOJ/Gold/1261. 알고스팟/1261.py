from heapq import *
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    heap = [(0, 0, 0)]
    while heap:
        c, y, x = heappop(heap)
        if (y, x) == (n - 1, m - 1):
            return c

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            visited[yy][xx] = 1
            heappush(heap, (c + arr[yy][xx], yy, xx))

    return -1


m, n = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
print(bfs())
