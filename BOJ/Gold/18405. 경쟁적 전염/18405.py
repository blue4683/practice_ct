from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs(s):
    virus = []
    for y in range(n):
        for x in range(n):
            if arr[y][x]:
                virus.append((arr[y][x], y, x))

    virus.sort()
    q = deque([(y, x) for _, y, x in virus])
    while s:
        s -= 1
        new_q = []
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or arr[yy][xx]:
                    continue

                arr[yy][xx] = arr[y][x]
                new_q.append((yy, xx))

        q = deque(new_q)
    return arr[ex - 1][ey - 1]


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, ex, ey = map(int, input().split())
print(bfs(s))
