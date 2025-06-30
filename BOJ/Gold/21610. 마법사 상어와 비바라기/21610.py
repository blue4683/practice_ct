import sys
input = sys.stdin.readline
direction = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1),
             (0, 1), (1, 1), (1, 0), (1, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
clouds = set([(n - 1 - i, j) for i in range(2) for j in range(2)])

for _ in range(m):
    d, s = map(int, input().split())
    rain = set()
    dy, dx = direction[d]
    for y, x in clouds:
        yy, xx = (y + dy * s) % n, (x + dx * s) % n
        rain.add((yy, xx))
        arr[yy][xx] += 1

    for y, x in rain:
        cnt = 0
        for i in range(2, 9, 2):
            dy, dx = direction[i]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or not arr[yy][xx]:
                continue

            cnt += 1

        arr[y][x] += cnt

    clouds = set()
    for y in range(n):
        for x in range(n):
            if (y, x) in rain:
                continue

            if arr[y][x] >= 2:
                arr[y][x] -= 2
                clouds.add((y, x))

print(sum(map(sum, arr)))
