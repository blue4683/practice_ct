import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(sy, sx, ey, ex):
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1
    q = [(sy, sx)]

    while q:
        y, x = q.pop()
        for i in range(4):
            if farm[y][x] & (1 << i):
                continue
            dy, dx = d[i]
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx]:
                if (yy, xx) == (ey, ex):
                    return 0

                visited[yy][xx] = 1
                q.append((yy, xx))

    return 1


n, k, r = map(int, input().split())
farm = [[0] * n for _ in range(n)]
for _ in range(r):
    y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())
    dy, dx = y2 - y1, x2 - x1
    farm[y1][x1] |= 1 << d.index((dy, dx))
    farm[y2][x2] |= 1 << d.index((-dy, -dx))

cows = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
result = 0
for i in range(k):
    y1, x1 = cows[i]
    for j in range(i + 1, k):
        y2, x2 = cows[j]
        result += bfs(y1, x1, y2, x2)

print(result)
