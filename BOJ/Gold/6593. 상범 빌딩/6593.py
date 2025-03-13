from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]


def out_of_range(z, y, x):
    if z < 0 or z >= l or y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def bfs():
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    visited[start[0]][start[1]][start[2]] = 1
    q = deque([start])
    while q:
        z, y, x = q.popleft()
        for dz, dy, dx in d:
            zz, yy, xx = z + dz, y + dy, x + dx
            if out_of_range(zz, yy, xx) or visited[zz][yy][xx] or building[zz][yy][xx] == '#':
                continue

            if (zz, yy, xx) == end:
                return f'Escaped in {visited[z][y][x]} minute(s).'

            visited[zz][yy][xx] = visited[z][y][x] + 1
            q.append((zz, yy, xx))

    return 'Trapped!'


while 1:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break

    building = []
    start, end = (0, 0, 0), (0, 0, 0)
    for z in range(l):
        floor = []
        for y in range(r):
            room = []
            for x, v in enumerate(input().rstrip()):
                if v == 'S':
                    start = (z, y, x)

                elif v == 'E':
                    end = (z, y, x)

                room.append(v)

            floor.append(room)

        building.append(floor)
        input()

    print(bfs())
