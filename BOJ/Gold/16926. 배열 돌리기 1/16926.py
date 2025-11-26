import sys
input = sys.stdin.readline
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for layer in range(min(n, m) // 2):
    left, right = layer, m - layer - 1
    top, bottom = layer, n - layer - 1
    tmp = []
    for x in range(left, right + 1):
        tmp.append(arr[top][x])

    for y in range(top + 1, bottom):
        tmp.append(arr[y][right])

    for x in range(right, left - 1, -1):
        tmp.append(arr[bottom][x])

    for y in range(bottom - 1, top, -1):
        tmp.append(arr[y][left])

    cnt = r % len(tmp)
    tmp = tmp[cnt:] + tmp[:cnt]
    idx = 0

    for x in range(left, right + 1):
        arr[top][x] = tmp[idx]
        idx += 1

    for y in range(top + 1, bottom):
        arr[y][right] = tmp[idx]
        idx += 1

    for x in range(right, left - 1, -1):
        arr[bottom][x] = tmp[idx]
        idx += 1

    for y in range(bottom - 1, top, -1):
        arr[y][left] = tmp[idx]
        idx += 1

for l in arr:
    print(*l)
