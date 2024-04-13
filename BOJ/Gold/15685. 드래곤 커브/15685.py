import sys
input = sys.stdin.readline

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def check(y, x):
    for dy in range(2):
        for dx in range(2):
            if arr[y + dy][x + dx] == 0:
                return 0

    return 1


def make_curve(x, y, d, g):
    arr[y][x] = 1
    path = [d]
    for _ in range(g):
        path += list(map(lambda x: (x + 1) % 4, path[::-1]))

    for p in path:
        dy, dx = dir[p]
        y += dy
        x += dx
        arr[y][x] = 1


n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * 101 for _ in range(101)]
for x, y, d, g in curves:
    make_curve(x, y, d, g)

result = 0
for y in range(100):
    for x in range(100):
        result += check(y, x)

print(result)
