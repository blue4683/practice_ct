from heapq import heappop, heappush
import sys
input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = 10 ** 9


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def on_bridge(y, x):
    if arr[y][x] > 1 or not arr[y][x]:
        return 1

    return 0


def bfs():
    heap = [(0, 0, 0, 0)]
    visited = [[[INF] * 2 for _ in range(n)] for _ in range(n)]
    visited[0][0] = [0, 0]
    while heap:
        t, used, y, x = heappop(heap)
        if (y, x) == (n - 1, n - 1):
            break

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx][used] <= t + 1:
                continue

            if on_bridge(y, x) and on_bridge(yy, xx):
                continue

            if arr[yy][xx] > 1 and (t + 1) % arr[yy][xx]:
                continue

            if not arr[yy][xx]:
                if used or (t + 1) % m:
                    continue

                possible = 0
                for dy, dx in d:
                    yyy, xxx = yy + dy, xx + dx
                    if (yyy, xxx) == (y, x):
                        continue

                    if not out_of_range(yyy, xxx) and arr[yyy][xxx] == 1:
                        possible = 1
                        break

                if not possible:
                    continue

            if arr[yy][xx]:
                visited[yy][xx][used] = t + 1
                heappush(heap, (t + 1, used, yy, xx))

            else:
                visited[yy][xx][1] = t + 1
                heappush(heap, (t + 1, 1, yy, xx))

        heappush(heap, (t + 1, used, y, x))

    return min(visited[n - 1][n - 1])


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(bfs())
