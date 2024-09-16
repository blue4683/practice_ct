import sys
input = sys.stdin.readline


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def throw_stick(y, is_right):
    if is_right:
        for x in range(c - 1, -1, -1):
            if cave[y][x] == 'x':
                cave[y][x] = '.'
                return

    else:
        for x in range(c):
            if cave[y][x] == 'x':
                cave[y][x] = '.'
                return


def get_hovered_cluster():
    visited = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if visited[y][x] or cave[y][x] == '.':
                continue

            cluster, visited, is_hovered = get_cluster(y, x, visited)
            if is_hovered:
                return cluster

    return []


def get_cluster(y, x, visited):
    cluster = [(y, x)]
    q = [(y, x)]
    visited[y][x] = 1
    is_hovered = y != r - 1

    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or cave[yy][xx] == '.' or visited[yy][xx]:
                continue

            visited[yy][xx] = 1
            cluster.append((yy, xx))
            q.append((yy, xx))
            if is_hovered and yy == r - 1:
                is_hovered = 0

    return cluster, visited, is_hovered


def update_cave(cluster):
    if not cluster:
        return

    cluster.sort(reverse=True)
    while 1:
        for y, x in cluster:
            yy = y + 1
            if out_of_range(yy, x) or cave[yy][x] == 'x' and (yy, x) not in cluster:
                return

        for i in range(len(cluster)):
            y, x = cluster[i]
            cave[y][x] = '.'
            cave[y + 1][x] = 'x'
            cluster[i] = (y + 1, x)


r, c = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(r)]
n = int(input())
for i, y in enumerate(map(int, input().split())):
    throw_stick(r - y, i % 2)
    hovered_cluster = get_hovered_cluster()
    update_cave(hovered_cluster)

for l in cave:
    print(''.join(l))
