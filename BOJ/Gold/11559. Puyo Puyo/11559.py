from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= 12 or x < 0 or x >= 6:
        return 1

    return 0


def is_chain(sy, sx):
    same = [(sy, sx)]
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] != arr[sy][sx] or visited[yy][xx]:
                continue

            visited[yy][xx] = 1
            same.append((yy, xx))
            q.append((yy, xx))

    if len(same) < 4:
        return []

    return same


arr = [list(input().rstrip()) for _ in range(12)]
result = 0
while 1:
    pos = []
    visited = [[0] * 6 for _ in range(12)]
    for y in range(11, -1, -1):
        for x in range(6):
            if arr[y][x] == '.' or visited[y][x]:
                continue

            visited[y][x] = 1
            popped = is_chain(y, x)
            if popped:
                pos.extend(popped)

    if not pos:
        break

    result += 1
    for y, x in pos:
        arr[y][x] = '.'

    for x in range(6):
        while 1:
            flag = 0
            for y in range(11, 0, -1):
                if arr[y][x] == '.' and arr[y - 1][x] != '.':
                    flag = 1
                    arr[y][x], arr[y - 1][x] = arr[y - 1][x], arr[y][x]

            if not flag:
                break

print(result)
