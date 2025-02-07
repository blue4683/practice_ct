from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (-1, 1), (-1, 0), (-1, -1),
     (0, -1), (1, -1), (1, 0), (1, 1), (0, 0)]


def out_of_range(y, x):
    if y < 0 or y >= 8 or x < 0 or x >= 8:
        return 1

    return 0


def move_arr(arr, move):
    if not move:
        return arr

    return [['.'] * 8 for _ in range(move)] + arr[:-move]


arr = [list(input().rstrip()) for _ in range(8)]
q = deque([(7, 0, 0)])
result = 0
while q:
    y, x, move = q.popleft()
    moved_arr = move_arr(arr, move)

    if moved_arr[y][x] == '#':
        continue

    if (y, x) == (0, 7):
        result = 1
        break

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx) or moved_arr[yy][xx] == '#':
            continue

        q.append((yy, xx, move + 1))

print(result)
