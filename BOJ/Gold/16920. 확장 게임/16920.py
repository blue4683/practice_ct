from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(pos, i):
    global flag
    q = deque()
    for y, x in pos:
        if visited[y][x]:
            continue

        q.append((y, x, 1))

    while q:
        y, x, cnt = q.popleft()
        visited[y][x] = 1
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] != '.':
                continue

            flag = 1
            arr[yy][xx] = str(i)
            pos.append((yy, xx))

            if cnt == s[i]:
                continue

            q.append((yy, xx, cnt + 1))

    return pos


n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
pos = [[] for _ in range(p + 1)]
for y in range(n):
    for x in range(m):
        if arr[y][x] not in ['.', '#']:
            pos[int(arr[y][x])].append((y, x))

while 1:
    flag = 0
    for i in range(1, p + 1):
        pos[i] = bfs(pos[i], i)

    if not flag:
        break

print(*map(len, pos[1:]))
