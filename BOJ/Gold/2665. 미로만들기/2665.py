from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs():
    visited = [[10 ** 9] * n for _ in range(n)]
    visited[0][0] = 1
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] <= visited[y][x] + (arr[yy][xx] ^ 1):
                continue

            visited[yy][xx] = visited[y][x] + (arr[yy][xx] ^ 1)
            q.append((yy, xx))

    return visited[n - 1][n - 1] - 1


n = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
print(bfs())
