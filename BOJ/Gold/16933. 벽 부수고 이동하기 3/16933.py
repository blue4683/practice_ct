from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0, 1, 0)])
    while q:
        y, x, cnt, day, wait = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            if (yy, xx) == (n - 1, m - 1):
                return visited[cnt][y][x] + 1

            if arr[yy][xx] == '1' and cnt < k:
                if day and not visited[cnt + 1][yy][xx]:
                    visited[cnt + 1][yy][xx] = visited[cnt][y][x] + 1 + wait
                    q.append((yy, xx, cnt + 1, day ^ 1, 0))

                if not day:
                    q.append((y, x, cnt, day ^ 1, 1))

            if arr[yy][xx] == '0' and not visited[cnt][yy][xx]:
                visited[cnt][yy][xx] = visited[cnt][y][x] + 1 + wait
                q.append((yy, xx, cnt, day ^ 1, 0))

    return -1


n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
if (n, m) == (1, 1):
    print(1)

else:
    print(bfs())
