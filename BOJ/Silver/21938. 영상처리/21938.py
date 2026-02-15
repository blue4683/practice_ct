from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs(sy, sx):
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or not arr[yy][xx] or visited[yy][xx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    return 1


n, m = map(int, input().split())
pixels = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

arr = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        rgb = sum(pixels[y][x * 3:x * 3 + 3]) / 3
        arr[y][x] = 1 if rgb >= t else 0

result = 0
visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if not arr[y][x] or visited[y][x]:
            continue

        visited[y][x] = 1
        result += bfs(y, x)

print(result)
