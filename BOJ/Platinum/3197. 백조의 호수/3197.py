from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def find(x):
    if graph[x] != x:
        return find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


def get_swan(num):
    global s, e
    if s == -1:
        s = num

    else:
        e = num


def numbering(y, x, num):
    q = deque([(y, x)])
    if lake[y][x] == 'L':
        get_swan(num)

    lake[y][x] = num
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or lake[yy][xx] == num:
                continue

            if lake[yy][xx] == 'X':
                ice.add((yy, xx))
                continue

            if lake[yy][xx] == 'L':
                get_swan(num)

            lake[yy][xx] = num
            q.append((yy, xx))


def melt(ice):
    next_melted = set()
    for y, x in ice:
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or (yy, xx) in next_melted:
                continue

            if lake[yy][xx] == 'X':
                next_melted.add((yy, xx))

            else:
                if lake[y][x] != 'X':
                    union(lake[y][x], lake[yy][xx])

                else:
                    lake[y][x] = lake[yy][xx]

    return next_melted


r, c = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(r)]
ice = set()

num = 1
s, e = -1, -1
for y in range(r):
    for x in range(c):
        if lake[y][x] not in ['.', 'L']:
            continue

        numbering(y, x, num)
        num += 1

graph = [i for i in range(num)]
time = 0
while find(s) != find(e):
    time += 1
    ice = melt(ice)

print(time)
