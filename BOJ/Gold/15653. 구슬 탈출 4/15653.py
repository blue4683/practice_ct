from collections import defaultdict, deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_red_first(i, yr, xr, yb, xb):
    if i == 0:
        return xr > xb

    if i == 1:
        return yr > yb

    if i == 2:
        return xr <= xb

    return yr <= yb


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    q = deque([(*red, *blue)])
    visited = defaultdict(int)
    visited[(*red, *blue)] = 1
    while q:
        yr, xr, yb, xb = q.popleft()
        for i in range(4):
            flag = 0
            dy, dx = d[i]
            yyr, xxr, yyb, xxb = yr, xr, yb, xb
            if is_red_first(i, yr, xr, yb, xb):
                while not out_of_range(yyr + dy, xxr + dx) and arr[yyr + dy][xxr + dx] != '#':
                    yyr, xxr = yyr + dy, xxr + dx
                    if arr[yyr][xxr] == 'O':
                        yyr, xxr = -1, -1
                        flag = 2
                        break

                while not out_of_range(yyb + dy, xxb + dx) and arr[yyb + dy][xxb + dx] != '#' and (yyb + dy, xxb + dx) != (yyr, xxr):
                    yyb, xxb = yyb + dy, xxb + dx
                    if arr[yyb][xxb] == 'O':
                        flag = 1
                        break

            else:
                while not out_of_range(yyb + dy, xxb + dx) and arr[yyb + dy][xxb + dx] != '#':
                    yyb, xxb = yyb + dy, xxb + dx
                    if arr[yyb][xxb] == 'O':
                        flag = 1
                        break

                while not out_of_range(yyr + dy, xxr + dx) and arr[yyr + dy][xxr + dx] != '#' and (yyr + dy, xxr + dx) != (yyb, xxb):
                    yyr, xxr = yyr + dy, xxr + dx
                    if arr[yyr][xxr] == 'O':
                        flag = 2
                        break

            if flag == 1 or visited[(yyr, xxr, yyb, xxb)]:
                continue

            elif flag == 2:
                return visited[(yr, xr, yb, xb)]

            else:
                if not visited[(yyr, xxr, yyb, xxb)]:
                    visited[(yyr, xxr, yyb, xxb)
                            ] = visited[(yr, xr, yb, xb)] + 1
                    q.append((yyr, xxr, yyb, xxb))

    return -1


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
red, blue = (0, ), (0, )
for y in range(n):
    for x in range(m):
        if arr[y][x] == 'B':
            blue = (y, x)

        elif arr[y][x] == 'R':
            red = (y, x)

print(bfs())
