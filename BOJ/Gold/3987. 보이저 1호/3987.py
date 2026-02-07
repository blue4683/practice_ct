from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9
d = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
index = {0: 'U', 1: 'R', 2: 'D', 3: 'L'}
change_d = {'/': [1, 0, 3, 2], '\\': [3, 2, 1, 0]}


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx, i):
    q = deque([(sy, sx, i)])
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    while q:
        y, x, direction = q.popleft()
        dy, dx = d[index[direction]]
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx) or arr[yy][xx] == 'C':
            continue

        dd = change_d[arr[yy][xx]][direction] if arr[yy][xx] in {
            '\\', '/'} else direction
        if visited[yy][xx][dd]:
            return INF

        visited[yy][xx][dd] = visited[y][x][direction] + 1
        q.append((yy, xx, dd))

    result = 0
    for y in range(n):
        for x in range(m):
            for direction in range(4):
                if visited[y][x][direction] + 1 > result:
                    result = visited[y][x][direction]

    return result + 1


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
sy, sx = map(lambda x: int(x) - 1, input().split())
result = 0
direction = ''
for i in range(4):
    tmp = bfs(sy, sx, i)
    if tmp > result:
        result = tmp
        direction = index[i]

print(direction)
print(result) if result != INF else print('Voyager')
