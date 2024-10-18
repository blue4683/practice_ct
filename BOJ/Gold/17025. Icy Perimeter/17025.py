import sys
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y > n + 1 or x < 0 or x > n + 1:
        return 1

    return 0


def check_blobs(sy, sx):
    area, perimeter = 1, 0
    visited[sy][sx] = 1
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            if machine[yy][xx] == '#':
                area += 1
                visited[yy][xx] = 1
                q.append((yy, xx))

            else:
                perimeter += 1

    return area, perimeter


n = int(input())
machine = [['.'] * (n + 2) for _ in range(n + 2)]
for y in range(1, n + 1):
    machine[y] = list('.' + input().rstrip() + '.')

result = (0, 10 ** 9)
visited = [[0] * (n + 2) for _ in range(n + 2)]
for y in range(1, n + 1):
    for x in range(1, n + 1):
        if machine[y][x] == '#' and not visited[y][x]:
            area, perimeter = check_blobs(y, x)
            if area > result[0] or area == result[0] and perimeter < result[1]:
                result = (area, perimeter)

print(*result)
