import sys
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def dfs(moves, y, x, visited):
    global result
    if moves == k:
        if (y, x) == (0, c - 1):
            result += 1

        return

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx) or arr[yy][xx] == 'T' or visited[yy][xx]:
            continue

        visited[yy][xx] = 1
        dfs(moves + 1, yy, xx, visited)
        visited[yy][xx] = 0


r, c, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
visited[r - 1][0] = 1
result = 0
dfs(1, r - 1, 0, visited)
print(result)
