import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def rotate():
    global arr
    tmp = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            tmp[n - 1 - x][y] = arr[y][x]

    arr = [l[:] for l in tmp]


def apply_gravity():
    for x in range(n):
        for y in range(n - 2, -1, -1):
            while y < n - 1 and arr[y][x] >= 0 and arr[y + 1][x] == -2:
                arr[y + 1][x], arr[y][x] = arr[y][x], arr[y + 1][x]
                y += 1


def get_block(sy, sx):
    rainbow = 0
    block = set()
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == -1 or (yy, xx) in block or (arr[yy][xx] and arr[yy][xx] != arr[sy][sx]):
                continue

            if arr[yy][xx]:
                visited[yy][xx] = 1

            else:
                rainbow += 1

            block.add((yy, xx))
            q.append((yy, xx))

    return ([], 0) if len(block) < 2 else (list(block), rainbow)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
while 1:
    visited = [[0] * n for _ in range(n)]
    max_block, max_rainbow = [], 0
    for y in range(n):
        for x in range(n):
            if arr[y][x] <= 0 or visited[y][x]:
                continue

            visited[y][x] = 1
            block, rainbow = get_block(y, x)
            if len(block) > len(max_block) or (len(block) == len(max_block) and rainbow >= max_rainbow):
                max_block = block[:]
                max_rainbow = rainbow

    if not max_block:
        break

    result += len(max_block) ** 2
    for y, x in max_block:
        arr[y][x] = -2

    apply_gravity()
    rotate()
    apply_gravity()

print(result)
