from collections import defaultdict
import sys
input = sys.stdin.readline

d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = defaultdict(int)


def rotate_dice(com):
    if com == 1:
        dice['up'], dice['right'], dice['down'], dice['left'] = dice['left'], dice['up'], dice['right'], dice['down']

    elif com == 2:
        dice['up'], dice['right'], dice['down'], dice['left'] = dice['right'], dice['down'], dice['left'], dice['up']

    elif com == 3:
        dice['up'], dice['front'], dice['down'], dice['back'] = dice['front'], dice['down'], dice['back'], dice['up']

    else:
        dice['up'], dice['front'], dice['down'], dice['back'] = dice['back'], dice['up'], dice['front'], dice['down']


n, m, y, x, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

for com in command:
    dy, dx = d[com]
    if 0 <= y + dy < n and 0 <= x + dx < m:
        yy, xx = y + dy, x + dx
        rotate_dice(com)
        if arr[yy][xx]:
            dice['down'] = arr[yy][xx]
            arr[yy][xx] = 0

        else:
            arr[yy][xx] = dice['down']

        print(dice['up'])
        y, x = yy, xx
