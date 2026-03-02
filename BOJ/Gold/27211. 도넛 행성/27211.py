from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(sy, sx):
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = (y + dy) % n, (x + dx) % m
            if arr[yy][xx]:
                continue

            arr[yy][xx] = 1
            q.append((yy, xx))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
for y in range(n):
    for x in range(m):
        if arr[y][x]:
            continue

        arr[y][x] = 1
        bfs(y, x)
        result += 1

print(result)
