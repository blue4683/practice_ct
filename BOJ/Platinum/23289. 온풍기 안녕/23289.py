from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def use_heater():
    for y, x, t in heaters:
        temp = [[0] * c for _ in range(r)]
        t -= 1
        directions = [(t,), (2, t), (3, t)] if t < 2 else [
            (t,), (0, t), (1, t)]
        dy, dx = d[t]
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx) or walls[y][x][yy][xx]:
            continue

        temp[yy][xx] = 5
        q = deque([(yy, xx)])
        while q:
            y, x = q.popleft()
            for direction in directions:
                yy, xx = y, x
                for i in direction:
                    dy, dx = d[i]
                    if out_of_range(yy + dy, xx + dx) or walls[yy][xx][yy + dy][xx + dx]:
                        break

                    yy, xx = yy + dy, xx + dx

                else:
                    temp[yy][xx] = temp[y][x] - 1
                    if temp[yy][xx] > 1:
                        q.append((yy, xx))

        for y in range(r):
            for x in range(c):
                arr[y][x] += temp[y][x]


def transfer_temp():
    temp = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or walls[y][x][yy][xx] or arr[y][x] < arr[yy][xx]:
                    continue

                side = (arr[y][x] - arr[yy][xx]) // 4
                temp[y][x] -= side
                temp[yy][xx] += side

    for y in range(r):
        for x in range(c):
            arr[y][x] += temp[y][x]

    visited = [[0] * c for _ in range(r)]
    for y in [0, r - 1]:
        for x in range(c):
            if not arr[y][x]:
                continue

            visited[y][x] = 1
            arr[y][x] -= 1

    for x in [0, c - 1]:
        for y in range(r):
            if not arr[y][x] or visited[y][x]:
                continue

            arr[y][x] -= 1


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
targets, heaters = [], []
for y in range(r):
    for x in range(c):
        if arr[y][x] == 5:
            targets.append((y, x))
            arr[y][x] = 0

        elif arr[y][x] > 0:
            heaters.append((y, x, arr[y][x]))
            arr[y][x] = 0

walls = [[[[0] * c for _ in range(r)] for _ in range(c)] for _ in range(r)]
for _ in range(int(input())):
    y, x, t = map(int, input().split())
    y, x = y - 1, x - 1
    if t:
        walls[y][x][y][x + 1] = 1
        walls[y][x + 1][y][x] = 1

    else:
        walls[y][x][y - 1][x] = 1
        walls[y - 1][x][y][x] = 1

result = 0
while result < 101:
    use_heater()
    transfer_temp()
    result += 1
    for y, x in targets:
        if arr[y][x] < k:
            break

    else:
        break

print(result)
