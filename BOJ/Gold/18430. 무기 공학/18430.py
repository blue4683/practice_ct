import sys
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def dfs(y, x, total):
    global result
    if x == m:
        x = 0
        y += 1

    if y == n:
        result = max(result, total)
        return

    if not visited[y][x]:
        for i in range(4):
            dy1, dx1 = d[i]
            dy2, dx2 = d[(i + 1) % 4]
            yy1, xx1 = y + dy1, x + dx1
            yy2, xx2 = y + dy2, x + dx2
            if out_of_range(yy1, xx1) or out_of_range(yy2, xx2) or visited[yy1][xx1] or visited[yy2][xx2]:
                continue

            visited[y][x] = 1
            visited[yy1][xx1] = 1
            visited[yy2][xx2] = 1

            boomerang = woods[y][x] * 2 + woods[yy1][xx1] + woods[yy2][xx2]
            dfs(y, x + 1, total + boomerang)

            visited[y][x] = 0
            visited[yy1][xx1] = 0
            visited[yy2][xx2] = 0

    dfs(y, x + 1, total)


n, m = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 0
dfs(0, 0, 0)

print(result)
