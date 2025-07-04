from collections import deque
import sys
input = sys.stdin.readline
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
num_to_pos = {}


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def mapping():
    dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num, y, x, direction = nn, 0, 0, 0
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1
    while num:
        num_to_pos[num] = (y, x)
        visited[y][x] = 1

        dy, dx = dd[direction]
        if out_of_range(y + dy, x + dx) or visited[y + dy][x + dx]:
            direction = (direction + 1) % 4
            dy, dx = dd[direction]

        y, x = y + dy, x + dx
        num -= 1


def blizzard(d, s):
    dy, dx = direction[d]
    for k in range(1, s + 1):
        yy, xx = sy + dy * k, sx + dx * k
        arr[yy][xx] = 0


def bomb():
    global result
    score = 0
    color, pos = 0, set()
    for i in range(2, nn + 1):
        y, x = num_to_pos[i]
        if not arr[y][x]:
            continue

        if arr[y][x] != color:
            if len(pos) >= 4:
                score += color * len(pos)
                for y, x in pos:
                    arr[y][x] = 0

            color = arr[y][x]
            pos = set()

        pos.add((y, x))

    if len(pos) >= 4:
        score += color * len(pos)
        for y, x in pos:
            arr[y][x] = 0

    if score:
        result += score
        bomb()

    return


def change():
    new_arr = [[0] * n for _ in range(n)]
    q = deque([])
    a, b = 0, 0
    for num in range(2, nn + 1):
        y, x = num_to_pos[num]
        if arr[y][x]:
            a = 1
            b = arr[y][x]
            break

    for i in range(num + 1, nn + 1):
        y, x = num_to_pos[i]
        if not arr[y][x]:
            continue

        if arr[y][x] == b:
            a += 1

        else:
            for k in [a, b]:
                q.append(k)

            a, b = 1, arr[y][x]

    for k in [a, b]:
        q.append(k)

    num = 2
    while q and num <= nn:
        y, x = num_to_pos[num]
        new_arr[y][x] = q.popleft()
        num += 1

    return new_arr


n, m = map(int, input().split())
nn = n ** 2
arr = [list(map(int, input().split())) for _ in range(n)]
mapping()

result = 0
sy, sx = n // 2, n // 2
for _ in range(m):
    d, s = map(int, input().split())
    blizzard(d - 1, s)
    bomb()
    arr = change()

print(result)
