import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def dfs(depth, y, x, sy, sx):
    global result
    if result == 'Yes':
        return

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if (yy, xx) == (sy, sx) and depth >= 4:
            result = 'Yes'
            return

        if out_of_range(yy, xx) or arr[yy][xx] != arr[sy][sx] or visited[yy][xx]:
            continue

        visited[yy][xx] = 1
        dfs(depth + 1, yy, xx, sy, sx)
        visited[yy][xx] = 0


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

result = 'No'
visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        visited[y][x] = 1
        dfs(1, y, x, y, x)

print(result)
