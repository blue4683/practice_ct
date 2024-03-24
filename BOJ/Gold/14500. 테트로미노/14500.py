import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find(depth, y, x, score):
    global result

    if depth == 3:
        result = max(result, score)
        return

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if 0 <= yy < n and 0 <= xx < m and not visited[yy][xx]:
            visited[yy][xx] = 1
            find(depth + 1, yy, xx, score + paper[yy][xx])
            visited[yy][xx] = 0


def find_t(y, x):
    global result

    score = paper[y][x]
    arr = []

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if 0 <= yy < n and 0 <= xx < m:
            arr.append(paper[yy][xx])

    arr.sort()
    if len(arr) == 4:
        result = max(result, score + sum(arr[1:]))

    elif len(arr) == 3:
        result = max(result, score + sum(arr))

    return


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 0

for y in range(n):
    for x in range(m):
        visited[y][x] = 1
        find(0, y, x, paper[y][x])
        find_t(y, x)
        visited[y][x] = 0

print(result)
