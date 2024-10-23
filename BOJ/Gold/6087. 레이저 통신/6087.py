from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 1

    return 0


def dijkstra(start, end):
    visited = [[[INF for _ in range(4)] for _ in range(w)] for _ in range(h)]
    for i in range(4):
        visited[start[0]][start[1]][i] = 0

    heap = [(0, i, *start) for i in range(4)]
    while heap:
        cnt, dir, y, x = heappop(heap)
        if visited[y][x][dir] != cnt:
            continue

        for k in range(4):
            if (k + 2) % 4 == dir:
                continue

            dy, dx = d[k]
            yy, xx = y + dy, x + dx
            ncnt = cnt
            if out_of_range(yy, xx) or arr[yy][xx] == '*':
                continue

            if k != dir:
                ncnt += 1

            if visited[yy][xx][k] > ncnt:
                visited[yy][xx][k] = ncnt
                heappush(heap, (ncnt, k, yy, xx))

    result = min([visited[end[0]][end[1]][i] for i in range(4)])
    return result


w, h = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(h)]
start, end = [(y, x) for y in range(h) for x in range(w) if arr[y][x] == 'C']
print(dijkstra(start, end))
