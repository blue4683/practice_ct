from collections import defaultdict, deque
import sys
input = sys.stdin.readline
shark_d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
fish_d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def out_of_range(y, x):
    if y < 0 or y >= 4 or x < 0 or x >= 4:
        return 1

    return 0


def move_fish(fish):
    moved = []
    for y, x, d in fish:
        cnt = 8
        while cnt:
            cnt -= 1
            dy, dx = fish_d[d]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or (yy, xx) == (sy, sx) or status[(yy, xx)] < 0:
                d = (d - 1) % 8

            else:
                arr[(y, x)] -= 1
                arr[(yy, xx)] += 1
                moved.append((yy, xx, d))
                break

        else:
            moved.append((y, x, d))

    return moved


def move_shark(sy, sx, fish):
    directions = []
    max_cnt = -1
    q = deque([(sy, sx, 0, [])])
    while q:
        y, x, cnt, moved = q.popleft()
        if len(moved) == 3:
            if cnt > max_cnt:
                max_cnt = cnt
                directions = moved[:]

            continue

        for i in range(4):
            dy, dx = shark_d[i]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            if (yy, xx) in moved:
                q.append((yy, xx, cnt, moved + [(yy, xx)]))

            else:
                q.append((yy, xx, cnt + arr[(yy, xx)], moved + [(yy, xx)]))

    if max_cnt > 0:
        removed = set()
        new_fish = []
        for y, x in directions:
            arr[(y, x)] = 0
            removed.add((y, x))

        for y, x, d in fish:
            if (y, x) in removed:
                status[(y, x)] = -3
                continue

            new_fish.append((y, x, d))

        fish = new_fish[:]

    sy, sx = directions[-1]
    return sy, sx, fish


m, s = map(int, input().split())
fish = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
sy, sx = map(lambda x: int(x) - 1, input().split())

status = defaultdict(int)
arr = defaultdict(int)
for y, x, _ in fish:
    arr[(y, x)] += 1

for _ in range(s):
    new_fish = fish[:]
    fish = move_fish(fish)
    sy, sx, fish = move_shark(sy, sx, fish)
    for pos in list(status.keys()):
        if status[pos]:
            status[pos] += 1

        if not status[pos]:
            del status[pos]

    for y, x, _ in new_fish:
        arr[(y, x)] += 1

    fish += new_fish

result = 0
for pos in arr.keys():
    result += arr[pos]

print(result)
