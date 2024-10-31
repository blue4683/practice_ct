import sys
input = sys.stdin.readline


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def rotate(r, c, sticker):
    new_sticker = [[0] * r for _ in range(c)]
    for y in range(c):
        for x in range(r):
            new_sticker[y][x] = sticker[r - 1 - x][y]

    return c, r, new_sticker


def paste(y, x, r, c, sticker):
    for dy in range(r):
        for dx in range(c):
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or sticker[dy][dx] and notebook[yy][xx]:
                return 0

    for dy in range(r):
        for dx in range(c):
            if sticker[dy][dx]:
                notebook[y + dy][x + dx] = 1

    return 1


def find(r, c, sticker):
    for _ in range(4):
        for y in range(n):
            for x in range(m):
                if paste(y, x, r, c, sticker):
                    return

        r, c, sticker = rotate(r, c, sticker)


n, m, k = map(int, input().split())
stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append([r, c, sticker])

notebook = [[0] * m for _ in range(n)]

for r, c, sticker in stickers:
    find(r, c, sticker)

print(sum(map(sum, notebook)))
