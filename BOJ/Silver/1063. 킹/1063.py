import sys
input = sys.stdin.readline
d = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
     'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}


def out_of_range(y, x):
    if y < 1 or y > 8 or x < 0 or x >= 8:
        return 1

    return 0


a, b, n = input().split()
pos = []
for x, y in [a, b]:
    yy, xx = int(y), ord(x) - ord('A')
    pos.append((yy, xx))

(sy, sx), (ey, ex) = pos
for _ in range(int(n)):
    direction = input().rstrip()
    dy, dx = d[direction]
    yy, xx = sy + dy, sx + dx
    if out_of_range(yy, xx):
        continue

    if (ey, ex) == (yy, xx):
        yyy, xxx = ey + dy, ex + dx
        if out_of_range(yyy, xxx):
            continue

        ey, ex = yyy, xxx

    sy, sx = yy, xx

print(chr(ord('A') + sx) + str(sy))
print(chr(ord('A') + ex) + str(ey))
