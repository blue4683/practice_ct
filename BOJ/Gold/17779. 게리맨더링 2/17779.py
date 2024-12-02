import sys
input = sys.stdin.readline


def out_of_range(x, y, d1, d2):
    if 0 <= x < x + d1 + d2 < n and 0 <= y - d1 < y < y + d2 < n:
        return 0

    return 1


def get_section(x, y, d1, d2):
    section = [[0] * n for _ in range(n)]
    for k in range(d1 + 1):
        section[x + k][y - k] = 5
        section[x + d2 + k][y + d2 - k] = 5

    for k in range(d2 + 1):
        section[x + k][y + k] = 5
        section[x + d1 + k][y - d1 + k] = 5

    return section


def get_population(ux, uy, d1, d2):
    section = get_section(ux, uy, d1, d2)
    population = [0] * 6
    for x in range(ux + d1):
        for y in range(uy + 1):
            if section[x][y]:
                break

            section[x][y] = 1

    for x in range(ux + d2 + 1):
        for y in range(n - 1, uy, -1):
            if section[x][y]:
                break

            section[x][y] = 2

    for x in range(ux + d1, n):
        for y in range(uy - d1 + d2):
            if section[x][y]:
                break

            section[x][y] = 3

    for x in range(ux + d2 + 1, n):
        for y in range(n - 1, uy - d1 + d2 - 1, -1):
            if section[x][y]:
                break

            section[x][y] = 4

    for x in range(n):
        for y in range(n):
            num = section[x][y] if section[x][y] else 5
            population[num] += city[x][y]

    return max(population[1:]) - min(population[1:])


n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
result = 10 ** 9
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if out_of_range(x, y, d1, d2):
                    break

                result = min(result, get_population(x, y, d1, d2))

print(result)
