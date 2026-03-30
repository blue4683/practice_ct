import sys
input = sys.stdin.readline
d = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def dfs(y, x):
    global result
    visited[y][x] = 1
    dy, dx = d[arr[y][x]]
    yy, xx = y + dy, x + dx
    if not visited[yy][xx]:
        dfs(yy, xx)

    elif visited[yy][xx] == 1:
        result += 1
        visited[y][x] = 2
        return

    visited[y][x] = 2
    return


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

result = 0
visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if visited[y][x]:
            continue

        dfs(y, x)

print(result)
