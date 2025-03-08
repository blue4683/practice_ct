from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 1

    return 0


def spread(q):
    n = len(q)
    for _ in range(n):
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] in ['#', '*']:
                continue

            arr[yy][xx] = '*'
            q.append((yy, xx))

    return q


def move():
    fire = deque([(y, x) for y in range(h)
                 for x in range(w) if arr[y][x] == '*'])
    q = deque([(y, x, 0) for y in range(h)
              for x in range(w) if arr[y][x] == '@'])
    visited = [[0] * w for _ in range(h)]
    visited[q[0][0]][q[0][1]] = 1
    while q:
        fire = spread(fire)
        n = len(q)
        for _ in range(n):
            y, x, cnt = q.popleft()
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx):
                    return cnt + 1

                if arr[yy][xx] in ['#', '*'] or visited[yy][xx]:
                    continue

                visited[yy][xx] = 1
                q.append((yy, xx, cnt + 1))

    return 'IMPOSSIBLE'


for _ in range(int(input())):
    w, h = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]

    print(move())
