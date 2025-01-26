import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def get_cluster(sy, sx):
    visited = [[0] * c for _ in range(r)]
    visited[sy][sx] = 1
    cluster = {(sy, sx)}
    q = [(sy, sx)]

    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or cave[yy][xx] == '.':
                continue

            visited[yy][xx] = 1
            cluster.add((yy, xx))
            q.append((yy, xx))

    h = 0
    while 1:
        h += 1
        for y, x in cluster:
            if (y + h, x) in cluster:
                continue

            if out_of_range(y + h, x) or cave[y + h][x] == 'x':
                return cluster, visited, h - 1


def fall():
    visited = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if cave[y][x] == '.' or visited[y][x]:
                continue

            cluster, visited, h = get_cluster(y, x)
            if not h:
                continue

            for y, x in sorted(cluster, key=lambda x: -x[0]):
                cave[y + h][x], cave[y][x] = cave[y][x], cave[y + h][x]

            return


def throw(h, is_right):
    if is_right:
        for x in range(c - 1, -1, -1):
            if cave[h][x] == '.':
                continue

            cave[h][x] = '.'
            fall()
            return

    else:
        for x in range(c):
            if cave[h][x] == '.':
                continue

            cave[h][x] = '.'
            fall()
            return


r, c = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(r)]
n = int(input())
sticks = list(map(int, input().split()))

for i, stick in enumerate(sticks):
    throw(r - stick, i % 2)

for l in cave:
    print(''.join(l))
