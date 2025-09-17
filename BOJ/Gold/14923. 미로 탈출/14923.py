from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    q = deque([(hy, hx, 0)])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[hy][hx][0] = 1
    while q:
        y, x, used = q.popleft()
        if (y, x) == (ey, ex):
            return visited[y][x][used] - 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx][used]:
                continue

            if not arr[yy][xx]:
                visited[yy][xx][used] = visited[y][x][used] + 1
                q.append((yy, xx, used))

            if arr[yy][xx] and not used:
                visited[yy][xx][1] = visited[y][x][used] + 1
                q.append((yy, xx, 1))

    return -1


n, m = map(int, input().split())
hy, hx = map(lambda x: int(x) - 1, input().split())
ey, ex = map(lambda x: int(x) - 1, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(bfs())
