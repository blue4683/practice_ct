import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= 5 or x < 0 or x >= 5:
        return 1

    return 0


def dfs(depth, y, x, num):
    global result
    if depth == 6:
        result.add(num + arr[y][x])
        return

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx):
            continue

        dfs(depth + 1, yy, xx, num + arr[y][x])


arr = [input().split() for _ in range(5)]
result = set()
for y in range(5):
    for x in range(5):
        dfs(1, y, x, '')

print(len(result))
