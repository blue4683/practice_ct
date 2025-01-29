from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= h + 2 or x < 0 or x >= w + 2:
        return 1

    return 0


def bfs(sy, sx):
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    q = deque([(sy, sx)])
    visited[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] != -1:
                continue

            if prison[yy][xx] in {'.', '$'}:
                visited[yy][xx] = visited[y][x]
                q.appendleft((yy, xx))

            elif prison[yy][xx] == '#':
                visited[yy][xx] = visited[y][x] + 1
                q.append((yy, xx))

    return visited


for _ in range(int(input())):
    h, w = map(int, input().split())
    prison = [list('.' * (w + 2))]
    for _ in range(h):
        prison.append(list('.' + input().rstrip() + '.'))

    prison.append(list('.' * (w + 2)))
    prisoner = []
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if prison[y][x] == '$':
                prisoner.append((y, x))

    visited1 = bfs(*prisoner[0])
    visited2 = bfs(*prisoner[1])
    visited3 = bfs(0, 0)

    result = 10 ** 9
    for y in range(h + 2):
        for x in range(w + 2):
            if prison[y][x] == '*' or -1 in {visited1[y][x], visited2[y][x], visited3[y][x]}:
                continue

            door = visited1[y][x] + visited2[y][x] + visited3[y][x]
            if prison[y][x] == '#':
                door -= 2

            result = min(result, door)

    print(result)
