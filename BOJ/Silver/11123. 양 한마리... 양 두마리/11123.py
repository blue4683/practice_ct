from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 1

    return 0


def bfs(sy, sx):
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx] != '#':
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))


for _ in range(int(input())):
    h, w = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    result = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and arr[y][x] == '#':
                visited[y][x] = 1
                result += 1
                bfs(y, x)

    print(result)
