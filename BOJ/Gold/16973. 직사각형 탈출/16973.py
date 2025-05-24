from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y + h > n or x < 0 or x + w > m:
        return 1

    return 0


def is_wall(y, x):
    for wy, wx in walls:
        if y <= wy < y + h and x <= wx < x + w:
            return 1

    return 0


def bfs(sy, sx, ey, ex):
    visited = [[10 ** 9] * m for _ in range(n)]
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        if (y, x) == (ey, ex):
            return visited[y][x] - 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] <= visited[y][x] + 1:
                continue

            if is_wall(yy, xx):
                visited[yy][xx] = 0
                continue

            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))

    return -1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
walls = [(y, x) for y in range(n) for x in range(m) if arr[y][x]]
h, w, sy, sx, ey, ex = map(int, input().split())
print(bfs(*map(lambda x: x - 1, [sy, sx, ey, ex])))
