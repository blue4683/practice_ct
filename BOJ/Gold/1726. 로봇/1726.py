from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def bfs():
    visited = [[[0] * 4 for _ in range(n)] for _ in range(m)]
    visited[sy][sx][sdir] = 1
    q = deque([(sy, sx, sdir)])
    while q:
        y, x, dir = q.popleft()
        if (y, x, dir) == (ey, ex, edir):
            return visited[y][x][dir] - 1

        dy, dx = d[dir]
        for k in range(1, 4):
            yy, xx = y + dy * k, x + dx * k
            if out_of_range(yy, xx) or arr[yy][xx]:
                break

            if visited[yy][xx][dir]:
                continue

            visited[yy][xx][dir] = visited[y][x][dir] + 1
            q.append((yy, xx, dir))

        rotation = [2, 3] if dir < 2 else [0, 1]
        for ddir in rotation:
            if visited[y][x][ddir]:
                continue

            visited[y][x][ddir] = visited[y][x][dir] + 1
            q.append((y, x, ddir))

    return -1


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
sy, sx, sdir = map(lambda x: int(x) - 1, input().split())
ey, ex, edir = map(lambda x: int(x) - 1, input().split())
print(bfs())
