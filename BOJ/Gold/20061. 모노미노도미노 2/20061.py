import sys
input = sys.stdin.readline


def out_of_range(y, x):
    if y >= 6 or x >= 6:
        return 1

    return 0


def move_green(block):
    for y, x in block:
        green[y][x] = 1

    while 1:
        tmp = []
        for y, x in block:
            if out_of_range(y + 1, x) or (y + 1, x) not in block and green[y + 1][x]:
                return

            tmp.append((y + 1, x))

        for y, x in block:
            green[y][x] = 0

        for y, x in tmp:
            green[y][x] = 1

        block = tmp[:]


def move_blue(block):
    for y, x in block:
        blue[y][x] = 1

    while 1:
        tmp = []
        for y, x in block:
            if out_of_range(y, x + 1) or (y, x + 1) not in block and blue[y][x + 1]:
                return

            tmp.append((y, x + 1))

        for y, x in block:
            blue[y][x] = 0

        for y, x in tmp:
            blue[y][x] = 1

        block = tmp[:]


def get_score():
    global score
    for y in range(2, 6):
        if sum(green[y]) != 4:
            continue

        score += 1
        for yy in range(y, 0, -1):
            green[yy] = green[yy - 1][:]

    for x in range(2, 6):
        if sum([blue[y][x] for y in range(4)]) != 4:
            continue

        score += 1
        for xx in range(x, 0, -1):
            for y in range(4):
                blue[y][xx] = blue[y][xx - 1]


def process_remain_green(n):
    for _ in range(n):
        if 1 not in green[1]:
            break

        for y in range(5, 0, -1):
            green[y] = green[y - 1][:]

        green[0] = [0] * 4


def process_remain_blue(n):
    for _ in range(n):
        if 1 not in [blue[y][1] for y in range(4)]:
            break

        for x in range(5, 0, -1):
            for y in range(4):
                blue[y][x] = blue[y][x - 1]

        for y in range(4):
            blue[y][0] = 0


def move(block):
    n = len(block)
    y1, x1 = block[0]
    green_block = [(0, x1)]
    blue_block = [(y1, 1)]
    if n == 2:
        y2, x2 = block[1]
        green_block.append((y1 - y2, x2))
        blue_block.append((y2, 1 - (x1 - x2)))

    move_green(green_block)
    move_blue(blue_block)

    get_score()

    process_remain_green(n)
    process_remain_blue(n)


green = [[0] * 4 for _ in range(6)]
blue = [[0] * 6 for _ in range(4)]
score = 0
for _ in range(int(input())):
    t, y, x = map(int, input().split())
    block = []
    if t == 2:
        block.append((y, x + 1))

    if t == 3:
        block.append((y + 1, x))

    block.append((y, x))
    move(block)

print(score)
print(sum(map(sum, green)) + sum(map(sum, blue)))
