from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def bfs(sy, sx):
    global result, fy, fx
    q = deque([(sy, sx)])
    visited[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == '#' or visited[yy][xx] != -1:
                continue

            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))
            if visited[yy][xx] > result:
                result = visited[yy][xx]
                fy, fx = yy, xx


for _ in range(int(input())):
    c, r = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(r)]
    visited = [[-1] * c for _ in range(r)]
    y, x = [(y, x) for y in range(r) for x in range(c) if arr[y][x] == '.'][0]
    result, fy, fx = 0, 0, 0
    bfs(y, x)

    visited = [[-1] * c for _ in range(r)]
    bfs(fy, fx)
    print(f'Maximum rope length is {result}.')
