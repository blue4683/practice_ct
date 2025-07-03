import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dice = {'up': 1, 'down': 6, 'left': 4, 'right': 3, 'front': 5, 'back': 2}


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def move(direction):
    if direction == 0:
        dice['up'], dice['right'], dice['down'], dice['left'] = dice['left'], dice['up'], dice['right'], dice['down']

    elif direction == 1:
        dice['up'], dice['back'], dice['down'], dice['front'] = dice['back'], dice['down'], dice['front'], dice['up']

    elif direction == 2:
        dice['up'], dice['right'], dice['down'], dice['left'] = dice['right'], dice['down'], dice['left'], dice['up']

    else:
        dice['up'], dice['back'], dice['down'], dice['front'] = dice['front'], dice['up'], dice['back'], dice['down']


def compare(y, x, direction):
    down = dice['down']
    if arr[y][x] < down:
        return (direction + 1) % 4

    elif arr[y][x] > down:
        return (direction - 1) % 4

    return direction


def get_score(sy, sx):
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1
    q = [(sy, sx)]
    cnt = 0
    while q:
        y, x = q.pop()
        cnt += 1
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx] != arr[sy][sx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    return cnt * arr[sy][sx]


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
y, x, direction = 0, 0, 0
result = 0
for _ in range(k):
    while 1:
        dy, dx = d[direction]
        yy, xx = y + dy, x + dx
        if not out_of_range(yy, xx):
            move(direction)
            break

        direction = (direction + 2) % 4

    result += get_score(yy, xx)
    direction = compare(yy, xx, direction)
    y, x = yy, xx

print(result)
