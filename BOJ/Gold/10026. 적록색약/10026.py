import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs(sy, sx, visited, blind):
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            if blind:
                if arr[y][x] in ['R', 'G'] and arr[yy][xx] in ['R', 'G'] or arr[y][x] == 'B' and arr[yy][xx] == 'B':
                    visited[yy][xx] = 1
                    q.append((yy, xx))

            else:
                if arr[yy][xx] == arr[y][x]:
                    visited[yy][xx] = 1
                    q.append((yy, xx))

    return visited


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

for i in range(2):
    result = 0
    visited = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue

            result += 1
            visited[y][x] = 1
            visited = bfs(y, x, visited, i)

    print(result, end=" ")
