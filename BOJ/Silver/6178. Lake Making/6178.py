import sys
input = sys.stdin.readline

r, c, e, n = map(int, input().split())
lake = [list(map(int, input().split())) for _ in range(r)]
pastures = []
for _ in range(n):
    rs, cs, ds = map(int, input().split())
    pastures.append((rs - 1, cs - 1, ds))

for y, x, d in pastures:
    max_height = 0
    for dy in range(3):
        for dx in range(3):
            max_height = max(max_height, lake[y + dy][x + dx] - d)

    for dy in range(3):
        for dx in range(3):
            if max_height > lake[y + dy][x + dx]:
                continue

            lake[y + dy][x + dx] = max_height

for y in range(r):
    for x in range(c):
        lake[y][x] = 0 if e - lake[y][x] < 0 else e - lake[y][x]

print(sum(map(sum, lake)) * (72 ** 2))
