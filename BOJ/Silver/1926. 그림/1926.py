import sys
input = sys.stdin.readline
d = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
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
            if out_of_range(yy, xx) or visited[yy][xx] or not arr[yy][xx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result, cnt = 0, 0

visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if visited[y][x] or not arr[y][x]:
            continue

        cnt += 1
        visited[y][x] = 1
        result = max(result, bfs(y, x))

print(cnt)
print(result)
