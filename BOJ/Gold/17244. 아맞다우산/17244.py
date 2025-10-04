from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def bfs():
    q = deque([(sy, sx, 0)])
    visited = [[[0] * n for _ in range(m)] for _ in range(1 << cnt)]
    visited[0][sy][sx] = 1
    while q:
        y, x, things = q.popleft()
        if things == (1 << cnt) - 1 and (y, x) == (ey, ex):
            return visited[things][y][x] - 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == '#' or visited[things][yy][xx]:
                continue

            if arr[yy][xx].isnumeric():
                visited[things | 1 << int(arr[yy][xx])
                        ][yy][xx] = visited[things][y][x] + 1
                q.append((yy, xx, things | 1 << int(arr[yy][xx])))

            else:
                visited[things][yy][xx] = visited[things][y][x] + 1
                q.append((yy, xx, things))

    return -1


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(m)]

sy, sx, ey, ex = -1, -1, -1, -1
cnt = 0
for y in range(m):
    for x in range(n):
        if arr[y][x] == 'X':
            arr[y][x] = str(cnt)
            cnt += 1

        elif arr[y][x] == 'S':
            sy, sx = y, x

        elif arr[y][x] == 'E':
            ey, ex = y, x

print(bfs())
