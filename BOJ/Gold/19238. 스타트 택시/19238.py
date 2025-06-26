from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs(sy, sx):
    global f
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1

    q = deque([(sy, sx)])
    dist, ey, ex = 10 ** 9, n, n
    while q:
        y, x = q.popleft()
        if (y, x) in customers:
            if (dist, ey, ex) > (visited[y][x] - 1, y, x):
                dist, ey, ex = visited[y][x] - 1, y, x

            continue

        if visited[y][x] - 1 >= dist:
            continue

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] or visited[yy][xx]:
                continue

            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))

    if dist == 10 ** 9:
        f = -1
        return -1, -1

    dest_y, dest_x = dests[(ey, ex)]
    e_dist = 10 ** 9
    visited = [[0] * n for _ in range(n)]
    visited[ey][ex] = 1
    q = deque([(ey, ex)])
    while q:
        y, x = q.popleft()
        if (y, x) == (dest_y, dest_x):
            e_dist = visited[y][x] - 1
            break

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] or visited[yy][xx]:
                continue

            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))

    if dist + e_dist > f:
        f = -1
        return -1, -1

    f += (e_dist - dist)
    customers.discard((ey, ex))
    return dest_y, dest_x


n, m, f = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sy, sx = map(lambda x: int(x) - 1, input().split())
dests = {}
for _ in range(m):
    y, x, yy, xx = map(lambda x: int(x) - 1, input().split())
    dests[(y, x)] = (yy, xx)

customers = set(dests.keys())
while customers and f > 0:
    sy, sx = bfs(sy, sx)

print(f)
