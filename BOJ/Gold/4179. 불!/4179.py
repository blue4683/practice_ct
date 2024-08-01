from collections import deque
import sys
input = sys.stdin.readline

d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if 0 <= y < r and 0 <= x < c:
        return 0

    return 1


def is_edge(y, x):
    if y in (0, r - 1) or x in (0, c - 1):
        return 1

    return 0


def bfs():
    q = deque(start_j)
    fire = deque(start_f)
    while fire:
        y, x = fire.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if not out_of_range(yy, xx) and not visited_f[yy][xx] and arr[yy][xx] in ['.', 'J']:
                arr[yy][xx] = 'F'
                visited_f[yy][xx] = visited_f[y][x] + 1
                fire.append((yy, xx))

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if not out_of_range(yy, xx) and not visited_j[yy][xx] and (not visited_f[yy][xx] or visited_f[yy][xx] > visited_j[y][x] + 1):
                visited_j[yy][xx] = visited_j[y][x] + 1
                if is_edge(yy, xx):
                    return visited_j[yy][xx]

                q.append((yy, xx))

    return 'IMPOSSIBLE'


r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
start_j = [(y, x) for y in range(r) for x in range(c) if arr[y][x] == 'J']
start_f = [(y, x) for y in range(r) for x in range(c) if arr[y][x] == 'F']
if is_edge(*start_j[0]):
    print(1)

else:
    visited_j = []
    visited_f = []
    for l in arr:
        visited_j.append(list(map(lambda x: 0 if x == '.' else 1, l)))
        visited_f.append(list(map(lambda x: 0 if x == '.' else 1, l)))

    print(bfs())
