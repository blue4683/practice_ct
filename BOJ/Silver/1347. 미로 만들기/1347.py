import sys
input = sys.stdin.readline
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]


n = int(input())
y, x = 0, 0
visited = {(y, x)}
drt = 0
for move in input().rstrip():
    if move == 'R':
        drt = (drt + 1) % 4

    elif move == 'L':
        drt = (drt - 1) % 4

    else:
        dy, dx = d[drt]
        y, x = y + dy, x + dx
        visited.add((y, x))

max_y, max_x, min_y, min_x = 0, 0, 50, 50
for y, x in visited:
    max_y = max(max_y, y)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    min_x = min(min_x, x)

arr = [['#'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
for y, x in visited:
    arr[y - min_y][x - min_x] = '.'

for l in arr:
    print(''.join(l))
