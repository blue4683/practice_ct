import sys
input = sys.stdin.readline


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def spread_seed(y, x):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx):
            continue

        tree[yy][xx].append(1)


def spend_spring():
    dead = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not tree[y][x]:
                continue

            tmp = []
            while tree[y][x]:
                age = tree[y][x].pop()
                if age > soil[y][x]:
                    dead[y][x] += age // 2
                    continue

                soil[y][x] -= age
                tmp.append(age + 1)

            tree[y][x] = sorted(tmp, reverse=True)

    return dead


def spend_summer(dead):
    for y in range(n):
        for x in range(n):
            soil[y][x] += dead[y][x]


def spend_autumn():
    for y in range(n):
        for x in range(n):
            for t in tree[y][x]:
                if t < 5:
                    break

                if t % 5:
                    continue

                spread_seed(y, x)


def spend_winter():
    for y in range(n):
        for x in range(n):
            soil[y][x] += food[y][x]


n, m, k = map(int, input().split())
soil = [[5] * n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
food = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    y, x, age = map(int, input().split())
    tree[y - 1][x - 1].append(age)
    tree[y - 1][x - 1].sort(reverse=True)

for _ in range(k):
    dead = spend_spring()
    spend_summer(dead)
    spend_autumn()
    spend_winter()

result = sum([sum(map(len, tree[y])) for y in range(n)])
print(result)
