from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    result = t + 1
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        y, x, s = q.popleft()
        if (y, x) == (n - 1, m - 1):
            result = visited[y][x][s] - 1
            break

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or (not s and arr[yy][xx] == 1) or visited[yy][xx][s]:
                continue

            if arr[yy][xx] == 2:
                visited[yy][xx][1] = visited[y][x][s] + 1
                q.append((yy, xx, 1))

            else:
                visited[yy][xx][s] = visited[y][x][s] + 1
                q.append((yy, xx, s))

    return 'Fail' if result > t else result


n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(bfs())
