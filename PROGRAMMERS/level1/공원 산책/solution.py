def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    y, x = [(y, x) for y in range(n) for x in range(m) if park[y][x] == 'S'][0]
    d = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    for route in routes:
        op, k = route.split()
        dy, dx = d[op]
        yy, xx = y, x
        for _ in range(int(k)):
            yy, xx = yy + dy, xx + dx
            if yy < 0 or yy >= n or xx < 0 or xx >= m or park[yy][xx] == 'X':
                break

        else:
            y, x = yy, xx

    answer = [y, x]
    return answer
