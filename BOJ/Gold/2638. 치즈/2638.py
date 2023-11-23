from collections import deque
import sys

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_border(sy, sx):
    q = deque([(sy, sx)])
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1
    pos = set()

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < m:
                if visited[yy][xx] == 0 and cheese[yy][xx] == 0:
                    visited[yy][xx] = 1
                    q.append((yy, xx))
                elif cheese[yy][xx] == 1:
                    visited[yy][xx] += 1
                    pos.add((yy, xx))

    for y, x in pos:
        if visited[y][x] > 1:
            cheese[y][x] = 0

    return


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

result = 0

while 1:
    find_border(0, 0)

    result += 1
    check = sum(map(lambda x: sum(x), cheese))
    if check == 0:
        print(result)
        break
