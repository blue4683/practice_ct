import sys
input = sys.stdin.readline

d = [(0, 0), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0),
     (0, 1), (-1, -1), (-1, 0), (-1, 1)]


def move_robots():
    global robots
    moved = []
    exploded = []
    for ry, rx in robots:
        board[ry][rx] = '.'
        if y - ry == 0:
            dy = 0

        else:
            dy = abs(y - ry) // (y - ry)

        if x - rx == 0:
            dx = 0

        else:
            dx = abs(x - rx) // (x - rx)

        ry, rx = ry + dy, rx + dx
        if board[ry][rx] == 'I':
            return 0

        if (ry, rx) in exploded:
            continue

        if (ry, rx) in moved:
            board[ry][rx] = '.'
            exploded.append((ry, rx))

        else:
            moved.append((ry, rx))

    robots = []
    for ry, rx in moved:
        if (ry, rx) in exploded:
            continue

        board[ry][rx] = 'R'
        robots.append((ry, rx))

    return 1


r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
y, x = [(y, x) for y in range(r) for x in range(c) if board[y][x] == 'I'][0]
robots = [(y, x) for y in range(r) for x in range(c) if board[y][x] == 'R']
directions = list(map(int, list(input().rstrip())))
result = 0

for i in range(len(directions)):
    direction = directions[i]
    board[y][x] = '.'
    dy, dx = d[direction]
    y, x = y + dy, x + dx
    if board[y][x] == 'R':
        result = i + 1
        break

    board[y][x] = 'I'
    if not move_robots():
        result = i + 1
        break

if result:
    print('kraj', result)

else:
    for l in board:
        print(''.join(l))
