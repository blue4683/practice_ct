from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx):
    result = 0
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx] == 'X':
                continue

            if arr[yy][xx] == 'P':
                result += 1

            visited[yy][xx] = 1
            q.append((yy, xx))

    return result if result else 'TT'


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
sy, sx = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'I'][0]
print(bfs(sy, sx))
