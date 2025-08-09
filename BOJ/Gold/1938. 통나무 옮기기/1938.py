from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x, is_row):
    k, l = is_row, is_row ^ 1
    if y < l or y >= n - l or x < k or x >= n - k:
        return 1

    return 0


def near_tree(y, x, is_row, is_rotate):
    k, l = is_row, is_row ^ 1
    if arr[y][x] or arr[y + l][x + k] or arr[y - l][x - k]:
        return 1

    if not is_rotate:
        return 0

    for dy, dx in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        yy, xx = y + dy, x + dx
        if arr[yy][xx]:
            return 1

    return 0


def bfs():
    sy, sx = log[1]
    is_row = int(log[0][0] == log[1][0])
    q = deque([(sy, sx, is_row)])
    visited = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    visited[sy][sx][is_row] = 1
    while q:
        y, x, is_row = q.popleft()
        if (y, x, is_row) == dest:
            return visited[y][x][is_row] - 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx, is_row) or near_tree(yy, xx, is_row, 0) or visited[yy][xx][is_row]:
                continue

            visited[yy][xx][is_row] = visited[y][x][is_row] + 1
            q.append((yy, xx, is_row))

        if not out_of_range(y, x, is_row ^ 1) and not near_tree(y, x, is_row ^ 1, 1) and not visited[y][x][is_row ^ 1]:
            visited[y][x][is_row ^ 1] = visited[y][x][is_row] + 1
            q.append((y, x, is_row ^ 1))

    return 0


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
log = []
dest = []

for y in range(n):
    for x in range(n):
        if arr[y][x] == 'B':
            log.append((y, x))
            arr[y][x] = '0'

        if arr[y][x] == 'E':
            dest.append((y, x))
            arr[y][x] = '0'

arr = [list(map(int, l)) for l in arr]
dest = (*dest[1], dest[1][0] == dest[0][0])
print(bfs())
