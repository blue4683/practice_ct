import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
pipes = {'|': {1: 1, 3: 3}, '-': {0: 0, 2: 2}, '+': {0: 0, 2: 2, 1: 1, 3: 3},
         '1': {3: 0, 2: 1}, '2': {1: 0, 2: 3}, '3': {0: 3, 1: 2}, '4': {0: 1, 3: 2}}


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def check():
    for y in range(r):
        for x in range(c):
            if europe[y][x] not in ['.', 'M', 'Z'] and not visited[y][x]:
                return 0
    return 1


def dfs(y, x, direction, pipe, py, px):
    global result
    if result:
        return

    dy, dx = d[direction]
    yy, xx = y + dy, x + dx
    if out_of_range(yy, xx):
        return

    if (yy, xx) == end:
        if check():
            result = [py + 1, px + 1, pipe]

        return

    if europe[yy][xx] not in ['.', 'M'] and direction in pipes[europe[yy][xx]].keys():
        visited[yy][xx] = 1
        dfs(yy, xx, pipes[europe[yy][xx]][direction], pipe, py, px)
        visited[yy][xx] = 0

    elif europe[yy][xx] == '.' and not pipe:
        for pipe in ['|', '-', '1', '2', '3', '4', '+']:
            if direction not in pipes[pipe].keys():
                continue

            visited[yy][xx] = 1
            europe[yy][xx] = pipe
            dfs(yy, xx, pipes[pipe][direction], pipe, yy, xx)
            europe[yy][xx] = '.'
            visited[yy][xx] = 0


r, c = map(int, input().split())
europe = [list(input().rstrip()) for _ in range(r)]

visited = [[0] * c for _ in range(r)]
y, x = [(y, x) for y in range(r) for x in range(c) if europe[y][x] == 'M'][0]
end = [(y, x) for y in range(r) for x in range(c) if europe[y][x] == 'Z'][0]

for i in range(4):
    dy, dx = d[i]
    yy, xx = y + dy, x + dx
    if out_of_range(yy, xx) or europe[yy][xx] in ['.', 'Z']:
        continue

    direction = i
    break

result = []
dfs(y, x, direction, '', 0, 0)
print(*result)
