from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs(start, end):
    result = INF
    sy, sx = start
    visited = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    q = deque()
    for i in range(4):
        visited[sy][sx][i] = 0
        q.append((sy, sx, i))

    while q:
        y, x, direction = q.popleft()
        if (y, x) == end:
            result = min(result, visited[y][x][direction])
            continue

        if house[y][x] == '*':
            continue

        elif house[y][x] == '!':
            for i in [-1, 1]:
                next_dir = (direction + i) % 4
                dy, dx = d[next_dir]
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or visited[yy][xx][next_dir] <= visited[y][x][direction] + 1:
                    continue

                visited[yy][xx][next_dir] = visited[y][x][direction] + 1
                q.append((yy, xx, next_dir))

        dy, dx = d[direction]
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx) or visited[yy][xx][direction] <= visited[y][x][direction]:
            continue

        visited[yy][xx][direction] = visited[y][x][direction]
        q.append((yy, xx, direction))

    return result


n = int(input())
house = [list(input().rstrip()) for _ in range(n)]
start, end = [(y, x) for y in range(n) for x in range(n) if house[y][x] == '#']
print(bfs(start, end))
