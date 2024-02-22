from collections import deque
import sys
input = sys.stdin.readline

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def find(sy, sx):
    global result
    q = deque([(sy, sx)])
    check = [(sy, sx)]

    while q:
        y, x = q.popleft()
        not_wall = []
        for i in range(4):
            if castle[y][x] & (1 << i) == 0:
                not_wall.append(d[i])

        for dy, dx in not_wall:
            yy, xx = y + dy, x + dx
            if 0 <= yy < m and 0 <= xx < n and not visited[yy][xx]:
                visited[yy][xx] = 1
                check.append((yy, xx))
                q.append((yy, xx))

    room_size = len(check)
    for y, x in check:
        visited[y][x] = (room_size, result[0])

    result[0] += 1
    result[1] = max(result[1], room_size)

    return


def check_visited():
    global result
    tmp = [[0] * n for _ in range(m)]
    tmp[0][0] = 1
    q = deque([(0, 0)])

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if 0 <= yy < m and 0 <= xx < n and not tmp[yy][xx]:
                tmp[yy][xx] = 1
                q.append((yy, xx))

                if visited[yy][xx] != visited[y][x]:
                    room_size = visited[yy][xx][0] + visited[y][x][0]
                    result[2] = max(result[2], room_size)

    return


n, m = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
result = [0, 0, 0]


for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            visited[y][x] = 1
            find(y, x)

check_visited()

for res in result:
    print(res)
