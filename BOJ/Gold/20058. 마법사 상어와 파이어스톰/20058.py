import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def get_mass(sy, sx):
    cnt = 1
    mass = arr[sy][sx]
    q = [(sy, sx)]
    visited[sy][sx] = 1
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or not arr[yy][xx] or visited[yy][xx]:
                continue

            mass += arr[yy][xx]
            cnt += 1
            visited[yy][xx] = 1
            q.append((yy, xx))

    return mass, cnt


def melt():
    melted = []
    for y in range(n):
        for x in range(n):
            if not arr[y][x]:
                continue

            cnt = 0
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or not arr[yy][xx]:
                    continue

                cnt += 1

            if cnt < 3:
                melted.append((y, x))

    for y, x in melted:
        arr[y][x] -= 1


def rotate(sy, sx, l):
    tmp = [[0] * l for _ in range(l)]
    for y in range(l):
        for x in range(l):
            tmp[x][l - 1 - y] = arr[sy + y][sx + x]

    for y in range(l):
        for x in range(l):
            arr[sy + y][sx + x] = tmp[y][x]


n, q = map(int, input().split())
n = 2 ** n
arr = [list(map(int, input().split())) for _ in range(n)]
for l in map(int, input().split()):
    if l:
        l = 2 ** l
        for y in range(0, n, l):
            for x in range(0, n, l):
                rotate(y, x, l)

    melt()

total = 0
mx = 0
visited = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if visited[y][x] or not arr[y][x]:
            continue

        mass, cnt = get_mass(y, x)
        total += mass
        mx = mx if mx > cnt else cnt

print(total)
print(mx)
