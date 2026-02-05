from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y > 500 or x < 0 or x > 500:
        return 1

    return 0


def bfs():
    visited = [[INF] * 501 for _ in range(501)]
    visited[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        life, y, x = heappop(heap)
        if life > visited[y][x]:
            continue

        if (y, x) == (500, 500):
            return life

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == -1:
                continue

            if visited[yy][xx] <= life + arr[yy][xx]:
                continue

            visited[yy][xx] = life + arr[yy][xx]
            heappush(heap, (life + arr[yy][xx], yy, xx))

    return -1


n = int(input())
arr = [[0] * 501 for _ in range(501)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2 + 1) if y1 < y2 else range(y2, y1 + 1):
        for x in range(x1, x2 + 1) if x1 < x2 else range(x2, x1 + 1):
            arr[y][x] = 1

m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2 + 1) if y1 < y2 else range(y2, y1 + 1):
        for x in range(x1, x2 + 1) if x1 < x2 else range(x2, x1 + 1):
            arr[y][x] = -1

print(bfs()) if (n, m) != (0, 0) else print(0)
