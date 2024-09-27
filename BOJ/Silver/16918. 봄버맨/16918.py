import sys
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]

r, c, n = map(int, input().split())
grid = [list(map(lambda x: 2 if x == 'O' else 0, input().rstrip()))
        for _ in range(r)]

n -= 1
time = 1
while time <= n:
    if time % 2 == 1:
        for y in range(r):
            for x in range(c):
                if not grid[y][x]:
                    grid[y][x] = 3

                elif grid[y][x] == 2:
                    grid[y][x] -= 1

    else:
        bombs = []
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 1:
                    bombs.append((y, x))

                else:
                    grid[y][x] -= 1

        for y, x in bombs:
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if 0 <= yy < r and 0 <= xx < c:
                    grid[yy][xx] = 0

    time += 1

for l in grid:
    print(''.join(map(lambda x: 'O' if x else '.', l)))
