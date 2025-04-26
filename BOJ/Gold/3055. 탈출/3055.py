from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def bfs():
    visited = [[0] * c for _ in range(r)]
    sy, sx, _ = s[0]
    visited[sy][sx] = 1
    q = deque(w + s)
    while q:
        y, x, is_water = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] in ['X', '*', 'S']:
                continue

            if is_water:
                if arr[yy][xx] == 'D':
                    continue

                arr[yy][xx] = '*'
                q.append((yy, xx, is_water))

            else:
                if arr[yy][xx] == 'D':
                    return visited[y][x]

                if visited[yy][xx]:
                    continue

                visited[yy][xx] = visited[y][x] + 1
                q.append((yy, xx, is_water))

    return 'KAKTUS'


r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
s = [(y, x, 0) for y in range(r) for x in range(c) if arr[y][x] == 'S']
w = [(y, x, 1) for y in range(r) for x in range(c) if arr[y][x] == '*']
print(bfs())
