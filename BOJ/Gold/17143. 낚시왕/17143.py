from collections import defaultdict
import sys
input = sys.stdin.readline

d = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
change_dir = {1: 2, 2: 1, 3: 4, 4: 3}


class Shark:
    def __init__(self, speed, dir, size):
        self.speed = speed
        self.dir = dir
        self.size = size

    def __lt__(self, other):
        return self.size < other.size


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def fishing(x):
    for y in range(r):
        if arr[(y, x)]:
            size = arr[(y, x)].size
            arr[(y, x)] = 0
            return size

    return 0


def move():
    new_arr = defaultdict(int)
    for y, x in arr.keys():
        if not arr[(y, x)]:
            continue

        shark = arr[(y, x)]
        dy, dx = d[shark.dir]
        for _ in range(shark.speed):
            if out_of_range(y + dy, x + dx):
                shark.dir = change_dir[shark.dir]
                dy, dx = d[shark.dir]

            y += dy
            x += dx

        if not new_arr[(y, x)] or new_arr[(y, x)] and new_arr[(y, x)] < shark:
            new_arr[(y, x)] = shark

    return new_arr


r, c, m = map(int, input().split())
arr = defaultdict(int)
for _ in range(m):
    y, x, *info = map(int, input().split())
    arr[(y - 1, x - 1)] = Shark(*info)

result = 0
for x in range(c):
    result += fishing(x)
    arr = move()

print(result)
