from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def bfs(sy, sx):
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or not arr[yy][xx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

result = 0
visited = [[0] * n for _ in range(m)]
for y in range(m):
    for x in range(n):
        if not arr[y][x] or visited[y][x]:
            continue

        result += 1
        visited[y][x] = 1
        bfs(y, x)

print(result)
