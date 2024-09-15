import sys
input = sys.stdin.readline

d = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def change_direction(dir):
    if dir % 2:
        return dir + 1

    return dir - 1


def move(num):
    y, x, dir = pieces[num]
    yy, xx = y + d[dir][0], x + d[dir][1]
    if out_of_range(yy, xx) or plate[yy][xx] == 2:
        dir = change_direction(dir)
        pieces[num][2] = dir

    yy, xx = y + d[dir][0], x + d[dir][1]
    if out_of_range(yy, xx) or plate[yy][xx] == 2:
        return 0

    elif plate[yy][xx] == 1:
        game[yy][xx].extend(game[y][x][::-1])
        game[y][x] = []

    else:
        game[yy][xx].extend(game[y][x])
        game[y][x] = []

    for i in game[yy][xx]:
        pieces[i - 1][0], pieces[i - 1][1] = yy, xx

    return 0 if len(game[yy][xx]) < 4 else 1


def play_game():
    turn = 1
    while turn <= 1000:
        for i in range(1, k + 1):
            y, x, _ = pieces[i - 1]
            if game[y][x][0] != i:
                continue

            if move(i - 1):
                return turn

        turn += 1

    return -1


n, k = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(n)]
game = [[[] for _ in range(n)] for _ in range(n)]
pieces = []
for i in range(1, k + 1):
    y, x, dir = map(int, input().split())
    y -= 1
    x -= 1
    pieces.append([y, x, dir])
    game[y][x].append(i)

print(play_game())
