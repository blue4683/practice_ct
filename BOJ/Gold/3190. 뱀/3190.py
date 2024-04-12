from collections import deque
import sys
input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (0, 1), (1, 0), (0, -1)]


def start_game():
    time = 1
    snake = deque([[0, 0]])
    changes = [0, 1]

    while 1:
        y, x = snake[0]
        dy, dx = changes
        yy, xx = y + dy, x + dx
        if yy < 0 or yy > n - 1 or xx < 0 or xx > n - 1:
            return time

        if [yy, xx] in snake:
            return time

        snake.appendleft([yy, xx])

        if directions and int(directions[0][0]) == time:
            _, c = directions.popleft()
            if c == 'L':
                dy, dx = d[d.index((dy, dx)) - 1]

            else:
                dy, dx = d[d.index((dy, dx)) + 1]

        changes = [dy, dx]

        if board[yy][xx]:
            board[yy][xx] = 0

        else:
            snake.pop()

        time += 1


n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
board = [[0] * n for _ in range(n)]
for y, x in apples:
    board[y - 1][x - 1] = 1

l = int(input())
directions = deque(list(input().split()) for _ in range(l))

print(start_game())
