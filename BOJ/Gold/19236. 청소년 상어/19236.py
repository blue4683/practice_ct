from copy import deepcopy
from collections import defaultdict
import sys
input = sys.stdin.readline
d = [(-1, 1), (-1, 0), (-1, -1), (0, -1),
     (1, -1), (1, 0), (1, 1), (0, 1)]


def out_of_range(y, x):
    if y < 0 or y >= 4 or x < 0 or x >= 4:
        return 1

    return 0


def move_fish(arr):
    idx = 0
    while idx < 16:
        fish = sorted(arr.items(), key=lambda x: x[1][0])
        for (y, x), (num, dir) in fish:
            if num <= idx:
                continue

            idx = num
            dy, dx = d[dir % 8]
            while out_of_range(y + dy, x + dx) or arr[(y + dy, x + dx)] == [-1, -1]:
                dir = (dir + 1) % 8
                dy, dx = d[dir % 8]

            arr[(y, x)][1] = dir
            yy, xx = y + dy, x + dx
            arr[(y, x)], arr[(yy, xx)] = arr[(yy, xx)], arr[(y, x)]
            break

        else:
            break

    return arr


def dfs(y, x, dir, total, arr):
    global result
    result = max(result, total)
    moved_arr = move_fish(deepcopy(arr))

    dy, dx = d[dir % 8]
    for k in range(1, 4):
        yy, xx = y + dy * k, x + dx * k
        if out_of_range(yy, xx):
            break

        if moved_arr[(yy, xx)] == [0, 0]:
            continue

        fish_num, fish_dir = moved_arr[(yy, xx)]
        moved_arr[(y, x)] = [0, 0]
        moved_arr[(yy, xx)] = [-1, -1]
        dfs(yy, xx, fish_dir, total + fish_num, moved_arr)
        moved_arr[(yy, xx)] = [fish_num, fish_dir]
        moved_arr[(y, x)] = [-1, -1]


arr = defaultdict(int)
for y in range(4):
    info = list(map(int, input().split()))
    for x in range(0, 8, 2):
        arr[(y, x // 2)] = info[x:x + 2]

num, dir = arr[(0, 0)]
arr[(0, 0)] = [-1, -1]
result = 0
dfs(0, 0, dir, num, arr)

print(result)
