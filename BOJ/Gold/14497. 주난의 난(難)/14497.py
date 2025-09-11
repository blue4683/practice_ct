from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    for t in range(1, n + m + 1):
        q = deque([(y1, x1)])
        visited = [[0] * m for _ in range(n)]
        visited[y1][x1] = 1
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or visited[yy][xx]:
                    continue

                if (yy, xx) == (y2, x2):
                    return t

                elif arr[yy][xx] == '1':
                    visited[yy][xx] = 1
                    arr[yy][xx] = '0'

                else:
                    visited[yy][xx] = 1
                    q.append((yy, xx))


n, m = map(int, input().split())
y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

print(bfs())
