from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def dijkstra():
    visited = [[[INF] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 0
    heap = [(0, 0, 0, 0)]
    while heap:
        moves, y, x, smell = heappop(heap)
        if visited[y][x][smell] != moves:
            continue

        for dir in range(4):
            dy, dx = d[dir]
            yy, xx, cost, nsmell = y + dy, x + dx, 1, smell
            if out_of_range(yy, xx) or not maze[yy][xx] or (maze[yy][xx] == 3 and not smell):
                continue

            if maze[yy][xx] == 2:
                nsmell = 1

            elif maze[yy][xx] == 4:
                nsmell = 0
                while maze[yy][xx] == 4 and not out_of_range(yy + dy, xx + dx) and maze[yy + dy][xx + dx] and (smell | maze[yy + dy][xx + dx] != 3):
                    yy, xx = yy + dy, xx + dx
                    cost += 1

            if visited[yy][xx][nsmell] > moves + cost:
                visited[yy][xx][nsmell] = moves + cost
                heappush(heap, (moves + cost, yy, xx, nsmell))

    result = min(visited[n - 1][m - 1][0], visited[n - 1][m - 1][1])
    return result if result != INF else -1


n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
print(dijkstra())
