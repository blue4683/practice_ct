import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 1

    return 0


def bfs(sy, sx):
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or not arr[yy][xx]:
                continue

            arr[yy][xx] = 0
            q.append((yy, xx))


while 1:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    for y in range(h):
        for x in range(w):
            if arr[y][x]:
                result += 1
                bfs(y, x)

    print(result)
