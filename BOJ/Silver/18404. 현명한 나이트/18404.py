from collections import deque
import sys
input = sys.stdin.readline
d = [(2, 1), (1, 2), (-2, 1), (-2, -1), (-1, -2), (-1, 2), (2, -1), (1, -2)]


def out_of_range(y, x):
    if y <= 0 or y > n or x <= 0 or x > n:
        return 1

    return 0


def bfs():
    q = deque([(sy, sx)])
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    visited[sy][sx] = 1
    result = [0] * m
    while q:
        y, x = q.popleft()
        if pieces.get((x, y)) is not None:
            result[pieces[(x, y)]] = visited[y][x] - 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))

    return result


n, m = map(int, input().split())
sx, sy = map(int, input().split())
pieces = {tuple(map(int, input().split())): i for i in range(m)}

result = bfs()
print(*result)
