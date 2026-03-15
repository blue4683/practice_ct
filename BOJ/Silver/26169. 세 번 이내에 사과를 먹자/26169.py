import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(y, x, cnt):
    global result
    if result:
        return

    if cnt == 2:
        result = 1
        return

    if visited[y][x] == 4:
        return

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if yy < 0 or yy >= 5 or xx < 0 or xx >= 5 or visited[yy][xx] or arr[yy][xx] == -1:
            continue

        visited[yy][xx] = visited[y][x] + 1
        dfs(yy, xx, cnt + arr[yy][xx])
        visited[yy][xx] = 0


arr = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

result = 0
visited = [[0] * 5 for _ in range(5)]
visited[r][c] = 1
dfs(r, c, arr[r][c])

print(result)
