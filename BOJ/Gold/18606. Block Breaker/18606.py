from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return 1

    return 0


def is_unstable(y, x, i):
    dy, dx = d[i]
    yy, xx = y + dy, x + dx
    return not out_of_range(yy, xx) and not frame[yy][xx]


def drop_blocks(sx, sy):
    if not frame[sy][sx]:
        return 0

    frame[sy][sx] = 0
    result = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        if frame[y][x] and is_unstable(y, x):
            result += 1
            frame[y][x] = 0

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or not frame[yy][xx]:
                continue

            if (is_unstable(yy, xx, 0) or is_unstable(yy, xx, 1)) and (is_unstable(yy, xx, 2) or is_unstable(yy, xx, 3)):
                frame[yy][xx] = 0
                result += 1
                q.append((yy, xx))

    return result


for _ in range(int(input())):
    n, m, q = map(int, input().split())
    frame = [[1] * n for _ in range(m)]
    for _ in range(q):
        print(drop_blocks(*map(lambda x: int(x) - 1, input().split())))
