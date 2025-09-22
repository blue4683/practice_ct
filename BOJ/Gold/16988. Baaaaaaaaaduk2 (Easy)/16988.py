from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx):
    cnt = 1
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            if arr[yy][xx] == 2:
                cnt += 1
                visited[yy][xx] = 1
                q.append((yy, xx))

            elif arr[yy][xx] == 0:
                cnt = -10 ** 9

    return cnt if cnt > 0 else 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
blank = [(y, x) for y in range(n) for x in range(m) if not arr[y][x]]
combs = combinations(blank, 2)
for (y1, x1), (y2, x2) in combs:
    tmp = 0
    arr[y1][x1], arr[y2][x2] = 1, 1
    visited = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 2 and not visited[y][x]:
                tmp += bfs(y, x)

    result = max(result, tmp)
    arr[y1][x1], arr[y2][x2] = 0, 0

print(result)
