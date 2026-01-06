from collections import deque
import sys
input = sys.stdin.readline
d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def bfs(sy, sx):
    visited = {(sy, sx)}
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        dy, dx = d[arr[y][x]]
        yy, xx = y + dy, x + dx
        if double_visited[yy][xx]:
            for y, x in visited:
                double_visited[y][x] = 1

            break

        if (yy, xx) in visited:
            for y, x in visited:
                double_visited[y][x] = 1

            return 1

        visited.add((yy, xx))
        q.append((yy, xx))

    return 0


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

double_visited = [[0] * m for _ in range(n)]
result = 0
for y in range(n):
    for x in range(m):
        if double_visited[y][x]:
            continue

        result += bfs(y, x)

print(result)
