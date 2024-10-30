import sys
input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def simulation(cases):
    flowers = 0
    gq = set([pos[i] for i in range(k) if cases[i] == 1])
    rq = set([pos[i] for i in range(k) if cases[i] == 2])
    visited = [[0] * m for _ in range(n)]

    while gq and rq:
        for y, x in gq:
            visited[y][x] = -1

        for y, x in rq:
            visited[y][x] = -1

        gvisited = set()
        rvisited = set()
        flowered = set()
        for y, x in gq:
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or not garden[yy][xx] or visited[yy][xx] in [-1, 1]:
                    continue

                visited[yy][xx] = 1
                gvisited.add((yy, xx))

        for y, x in rq:
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or not garden[yy][xx] or visited[yy][xx] in [-1, 2]:
                    continue

                if visited[yy][xx] == 1:
                    flowers += 1
                    flowered.add((yy, xx))
                    visited[yy][xx] = -1
                    continue

                visited[yy][xx] = 2
                rvisited.add((yy, xx))

        gvisited -= flowered
        gq, rq = gvisited, rvisited

    return flowers


def find_cases(depth, green, red, cases):
    global result
    if depth == k:
        if not green and not red:
            result = max(result, simulation(cases))

        return

    find_cases(depth + 1, green, red, cases)
    if green:
        cases[depth] = 1
        find_cases(depth + 1, green - 1, red, cases)
        cases[depth] = 0

    if red:
        cases[depth] = 2
        find_cases(depth + 1, green, red - 1, cases)
        cases[depth] = 0


n, m, g, r = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]
pos = [(y, x) for y in range(n) for x in range(m) if garden[y][x] == 2]
k = len(pos)

result = 0
find_cases(0, g, r, [0] * k)
print(result)
