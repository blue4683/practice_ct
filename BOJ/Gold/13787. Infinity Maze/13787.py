import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

cardinal = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dir_to_str(dir):
    for key, value in cardinal.items():
        if value == dir:
            dir = key
            break

    return dir


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w or maze[y][x] == '#':
        return 1

    return 0


def dfs(y, x, dir, depth):
    global sy, sx, sdir, cycle
    if visited[dir][y][x] != -1:
        sy, sx, sdir = y, x, dir
        cycle = depth - visited[dir][y][x]
        return

    visited[dir][y][x] = depth
    if depth == l:
        sy, sx, sdir = y, x, dir
        return

    while 1:
        if not out_of_range(y + d[dir][0], x + d[dir][1]):
            break

        dir = (dir + 1) % 4

    dy, dx = d[dir]
    y, x = y + dy, x + dx
    dfs(y, x, dir, depth + 1)


while 1:
    h, w, l = map(int, input().split())
    if (h, w, l) == (0, 0, 0):
        break

    maze = [list(input().rstrip()) for _ in range(h)]
    sy, sx = [(y, x) for y in range(h)
              for x in range(w) if maze[y][x] not in ['.', '#']][0]
    sdir = cardinal[maze[sy][sx]]

    visited = [[[-1] * w for _ in range(h)] for _ in range(4)]
    cycle = 0
    dfs(sy, sx, sdir, 0)

    if not cycle:
        print(sy + 1, sx + 1, dir_to_str(sdir))

    else:
        remain = (l - visited[sdir][sy][sx]) % cycle
        for _ in range(remain):
            while 1:
                if not out_of_range(sy + d[sdir][0], sx + d[sdir][1]):
                    break

                sdir = (sdir + 1) % 4

            dy, dx = d[sdir]
            sy, sx = sy + dy, sx + dx

        print(sy + 1, sx + 1, dir_to_str(sdir))
