import sys
input = sys.stdin.readline

d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r + 2 or x < 0 or x >= c + 2:
        return 1

    return 0


def bfs(height):
    q = [(0, 0)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or h[yy][xx] >= height:
                continue

            h[yy][xx] = height
            q.append((yy, xx))

    return


for t in range(int(input())):
    r, c = map(int, input().split())
    h = [[0] * (c + 2) for _ in range(r + 2)]
    max_height = 0
    for y in range(1, r + 1):
        arr = list(map(int, input().split()))
        for x in range(c):
            h[y][x + 1] = arr[x]
            max_height = max(max_height, arr[x])

    result = 0
    for height in range(1, max_height + 1):
        bfs(height)
        for y in range(1, r + 1):
            for x in range(1, c + 1):
                if h[y][x] >= height:
                    continue

                h[y][x] = height
                result += 1

    print(f'Case #{t + 1}: {result}')
