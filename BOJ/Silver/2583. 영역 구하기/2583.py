import sys
input = sys.stdin.readline
d = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def bfs(sy, sx):
    cnt = 0
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        cnt += 1
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] or visited[yy][xx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    return cnt


m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for x1, y1, x2, y2 in [list(map(int, input().split())) for _ in range(k)]:
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 1

result = []
visited = [[0] * n for _ in range(m)]
for y in range(m):
    for x in range(n):
        if arr[y][x] or visited[y][x]:
            continue

        visited[y][x] = 1
        result.append(bfs(y, x))

result.sort()
print(len(result))
print(*result)
