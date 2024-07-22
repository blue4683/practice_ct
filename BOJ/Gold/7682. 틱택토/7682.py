import sys
input = sys.stdin.readline


def check_end(flag):
    for i in range(0, 9, 3):
        line = boards[i:i + 3]
        if line == flag * 3:
            return 1

    for i in range(3):
        line = boards[i] + boards[i + 3] + boards[i + 6]
        if line == flag * 3:
            return 1

    cross = [boards[0] + boards[4] + boards[8],
             boards[2] + boards[4] + boards[6]]

    if flag * 3 in cross:
        return 1

    return 0


def tictactoe():
    o, x = 0, 0
    for s in boards:
        if s == 'O':
            o += 1

        if s == 'X':
            x += 1

    if o > 4 or x > 5:
        return 0

    if x - o < 0 or x - o > 1:
        return 0

    if x == o and check_end('O') and not check_end('X'):
        return 1

    if x - o == 1 and check_end('X') and not check_end('O'):
        return 1

    if (o, x) == (4, 5) and not check_end('O'):
        return 1

    return 0


while 1:
    boards = input().rstrip()
    if boards == 'end':
        break

    if tictactoe():
        print('valid')

    else:
        print('invalid')
