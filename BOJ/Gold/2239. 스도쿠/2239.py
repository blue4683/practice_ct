import sys

input = sys.stdin.readline


def check(y, x, num):
    for i in range(9):
        if sudoku[y][i] == num or sudoku[i][x] == num:
            return False

    yy, xx = 3 * (y // 3), 3 * (x // 3)

    for i in range(3):
        for j in range(3):
            if sudoku[yy + i][xx + j] == num:
                return False

    return True


def dfs(depth):
    if depth >= n:
        for l in sudoku:
            print("".join(map(str, l)))
        exit()

    y, x = pos[depth]

    for i in range(1, 10):
        if check(y, x, i):
            sudoku[y][x] = i
            dfs(depth + 1)
            sudoku[y][x] = 0


sudoku = [list(map(int, list(input().strip()))) for _ in range(9)]
pos = [(y, x) for y in range(9) for x in range(9) if sudoku[y][x] == 0]
n = len(pos)

dfs(0)
