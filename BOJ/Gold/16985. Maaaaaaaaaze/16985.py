from collections import deque
from itertools import permutations, product
import sys
input = sys.stdin.readline
d = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]


def rotate(i, arr):
    for _ in range(i):
        new_arr = [[0] * 5 for _ in range(5)]
        for y in range(5):
            for x in range(5):
                new_arr[4 - x][y] = arr[y][x]

        arr = [l[:] for l in new_arr]

    return arr


def out_of_range(z, y, x):
    if z < 0 or z >= 5 or y < 0 or y >= 5 or x < 0 or x >= 5:
        return 1

    return 0


def bfs(arr):
    if not arr[0][0][0] or not arr[4][4][4]:
        return 10 ** 9

    q = deque([(0, 0, 0)])
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1

    while q:
        z, y, x = q.popleft()
        if visited[z][y][x] >= result:
            continue

        if (z, y, x) == (4, 4, 4):
            return visited[z][y][x] - 1

        for dz, dy, dx in d:
            zz, yy, xx = z + dz, y + dy, x + dx
            if out_of_range(zz, yy, xx) or visited[zz][yy][xx] or not arr[zz][yy][xx]:
                continue

            visited[zz][yy][xx] = visited[z][y][x] + 1
            q.append((zz, yy, xx))

    return 10 ** 9


maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

result = 10 ** 9
orders = list(permutations(range(5)))
rotate_orders = list(product(range(4), repeat=5))
for order in orders:
    for rotate_order in rotate_orders:
        arr = [rotate(i, maze[z]) for z, i in zip(order, rotate_order)]
        result = min(result, bfs(arr))
        if result == 12:
            print(result)
            exit()

print(result if result != 10 ** 9 else -1)
