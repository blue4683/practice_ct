from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
change = [{}, {0: 2, 2: 0, 1: 1, 3: 3}, {0: 0, 2: 2, 1: 3, 3: 1},
          {0: 3, 1: 2, 2: 1, 3: 0}, {0: 1, 1: 0, 2: 3, 3: 2}]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    q = deque()
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    for y, x in s:
        for i in range(4):
            visited[y][x][i] = 1
            q.append((i, y, x))

    while q:
        drt, y, x = q.popleft()
        dy, dx = d[drt]
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx) or visited[yy][xx][drt]:
            continue

        visited[yy][xx][drt] = 1
        turn = change[arr[yy][xx]][drt] if arr[yy][xx] else drt
        q.append((turn, yy, xx))

    return sum(sum(any(l) for l in row) for row in visited)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 9]
print(bfs())
