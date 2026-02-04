from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    visited = [[[INF] * 2 for _ in range(m)] for _ in range(n)]
    for i in range(2):
        visited[sy][sx][i] = 0

    heap = [(0, 0, sy, sx)]
    while heap:
        g, ng, y, x = heappop(heap)
        if (y, x) == (ey, ex):
            return g, ng

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            garbage = int(arr[yy][xx] == 'g')
            near = 0
            if arr[yy][xx] == '.':
                for dy, dx in d:
                    yyy, xxx = yy + dy, xx + dx
                    if not out_of_range(yyy, xxx) and arr[yyy][xxx] == 'g':
                        near = 1
                        break

            if (visited[yy][xx][0], visited[yy][xx][1]) > (g + garbage, ng + near):
                visited[yy][xx][0] = g + garbage
                visited[yy][xx][1] = ng + near
                heappush(heap, (g + garbage, ng + near, yy, xx))


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
for y in range(n):
    for x in range(m):
        if arr[y][x] == 'S':
            sy, sx = y, x

        elif arr[y][x] == 'F':
            ey, ex = y, x

print(*bfs())
