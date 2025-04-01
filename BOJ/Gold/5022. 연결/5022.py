from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y > n or x < 0 or x > m:
        return 1

    return 0


def bfs(s, e, arr, first):
    sy, sx = s
    visited = [[(0, 0, 0) for _ in range(m + 1)] for _ in range(n + 1)]
    q = deque([(*s, 0)])
    while q:
        y, x, c = q.popleft()
        if (y, x) == e:
            if first:
                while (y, x) != s:
                    y, x = visited[y][x][:2]
                    arr[y][x] = arr[sy][sx]

            return c, arr

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] != (0, 0, 0):
                continue

            if arr[yy][xx] and arr[yy][xx] != arr[sy][sx]:
                continue

            visited[yy][xx] = (y, x, c + 1)
            q.append((yy, xx, c + 1))

    return -1, arr


def get_dist(s, e, ss, ee, arr):
    result, arr = bfs(s, e, arr, 1)
    cnt, _ = bfs(ss, ee, arr, 0)
    if cnt == -1:
        return 10 ** 9

    return result + cnt


n, m = map(int, input().split())
a1, a2, b1, b2 = [tuple(map(int, input().split())) for _ in range(4)]
arr = [[0] * (m + 1) for _ in range(n + 1)]
for y, x in [a1, a2]:
    arr[y][x] = 1

for y, x in [b1, b2]:
    arr[y][x] = 2

result = 10 ** 9
cnt1 = get_dist(a1, a2, b1, b2, [l[:] for l in arr])
cnt2 = get_dist(b1, b2, a1, a2, [l[:] for l in arr])

result = min(result, cnt1, cnt2)
print(result) if result != 10 ** 9 else print('IMPOSSIBLE')
