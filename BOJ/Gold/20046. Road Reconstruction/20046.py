from heapq import heappop, heappush
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 10 ** 9


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def dijkstra():
    if -1 in {arr[0][0], arr[m - 1][n - 1]}:
        return -1

    heap = [(arr[0][0], 0, 0)]
    dists = [[INF] * n for _ in range(m)]
    dists[0][0] = arr[0][0]
    while heap:
        dist, y, x = heappop(heap)
        if dist > dists[y][x]:
            continue

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == -1 or dists[yy][xx] <= dist + arr[yy][xx]:
                continue

            dists[yy][xx] = dist + arr[yy][xx]
            heappush(heap, (dist + arr[yy][xx], yy, xx))

    return dists[m - 1][n - 1] if dists[m - 1][n - 1] != INF else -1


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

print(dijkstra())
