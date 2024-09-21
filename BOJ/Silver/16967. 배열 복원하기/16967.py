import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h + x)]

a = [[0] * w for _ in range(h)]

for yy in range(x):
    for xx in range(w):
        a[yy][xx] = b[yy][xx]

for yy in range(h):
    for xx in range(y):
        a[yy][xx] = b[yy][xx]

for yy in range(x, h):
    for xx in range(y, w):
        a[yy][xx] = b[yy][xx] - a[yy - x][xx - y]

for l in a:
    print(*l)
