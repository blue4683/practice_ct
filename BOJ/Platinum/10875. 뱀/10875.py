import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def crossed(i, j):
    global collided
    x1, y1, x2, y2 = lines[i]
    x3, y3, x4, y4 = lines[j]
    if min(x1, x2) > max(x3, x4) or min(x3, x4) > max(x1, x2) or min(y1, y2) > max(y3, y4) or min(y3, y4) > max(y1, y2):
        return INF

    collided = 1
    if x1 == x2:
        return min(abs(y3 - y1), abs(y4 - y1)) + 1

    return min(abs(x3 - x1), abs(x4 - x1)) + 1


l, n = int(input()), int(input())
L = l + 1
lines = [(-L, L, L, L), (-L, -L, L, -L),
         (L, -L, L, L), (-L, -L, -L, L), (0, 0, 0, 0)]
directions = [0]
collided = 0
time = 0

for i in range(5, n + 5):
    t, k = input().split()
    if collided:
        continue

    t = int(t)
    k = 1 if k == 'R' else -1
    dir = (directions[-1] + k) % 4
    directions.append(dir)

    _, _, x2, y2 = lines[-1]
    if directions[-2] == 0:
        lines.append((x2 + 1, y2, x2 + t, y2))

    elif directions[-2] == 1:
        lines.append((x2, y2 + 1, x2, y2 + t))

    elif directions[-2] == 2:
        lines.append((x2 - 1, y2, x2 - t, y2))

    else:
        lines.append((x2, y2 - 1, x2, y2 - t))

    x = INF
    for j in range(i):
        x = min(x, crossed(i, j))

    time += x if collided else t

if not collided:
    t = 3 * l
    _, _, x2, y2 = lines[-1]
    if directions[-1] == 0:
        lines.append((x2 + 1, y2, x2 + t, y2))

    elif directions[-1] == 1:
        lines.append((x2, y2 + 1, x2, y2 + t))

    elif directions[-1] == 2:
        lines.append((x2 - 1, y2, x2 - t, y2))

    else:
        lines.append((x2, y2 - 1, x2, y2 - t))

    x = INF
    for j in range(n + 5):
        x = min(x, crossed(n + 5, j))

    time += x

print(time)
