import sys
input = sys.stdin.readline


def win_x(x, o):
    return 1 if x - o == 1 else 0


def win_o(x, o):
    return 1 if x == o else 0


def is_possible(arr, xcnt, ocnt):
    if xcnt - ocnt not in [0, 1]:
        return 0

    diagonal = ''
    inverse = ''
    for y in range(3):
        diagonal += arr[y][y]
        inverse += arr[y][2 - y]
        if arr[y] == ['X'] * 3:
            return win_x(xcnt, ocnt)

        elif arr[y] == ['O'] * 3:
            return win_o(xcnt, ocnt)

        col = ''
        for x in range(3):
            col += arr[x][y]

        if col == 'XXX':
            return win_x(xcnt, ocnt)

        elif col == 'OOO':
            return win_o(xcnt, ocnt)

    if diagonal == 'XXX':
        return win_x(xcnt, ocnt)

    elif diagonal == 'OOO':
        return win_o(xcnt, ocnt)

    if inverse == 'XXX':
        return win_x(xcnt, ocnt)

    elif inverse == 'OOO':
        return win_o(xcnt, ocnt)

    return 1


t = int(input())
for i in range(t):
    grid = [list(input().rstrip()) for _ in range(3)]
    if i != t - 1:
        input()

    result = 'no'
    xcnt, ocnt = 0, 0
    for y in range(3):
        for x in range(3):
            if grid[y][x] == 'X':
                xcnt += 1

            elif grid[y][x] == 'O':
                ocnt += 1

    if is_possible(grid, xcnt, ocnt):
        print('yes')

    else:
        print('no')
