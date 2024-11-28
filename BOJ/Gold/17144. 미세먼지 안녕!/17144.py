import sys
input = sys.stdin.readline
d = [(1, 0), (0, -1), (0, 1), (-1, 0)]
cw = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ccw = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def spread(dusts):
    spreaded = [[0] * c for _ in range(r)]
    for y, x in dusts:
        dust = room[y][x] // 5
        if not dust:
            continue

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or room[yy][xx] == -1:
                continue

            spreaded[yy][xx] += dust
            spreaded[y][x] -= dust

    for y in range(r):
        for x in range(c):
            room[y][x] += spreaded[y][x]


def circulate(purifier):
    for i in range(2):
        y, x = purifier[i]
        tmp = 0
        dir = 0
        while 1:
            dy, dx = ccw[dir] if not i else cw[dir]
            if out_of_range(y + dy, x + dx):
                dir += 1
                continue

            y, x = y + dy, x + dx
            if room[y][x] == -1:
                break

            room[y][x], tmp = tmp, room[y][x]


r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
purifier = sorted([(y, x) for y in range(r)
                  for x in range(c) if room[y][x] == -1])

for _ in range(t):
    spread([(y, x) for y in range(r) for x in range(c) if room[y][x] > 0])
    circulate(purifier)

print(sum(map(sum, room)) + 2)
