import sys
input = sys.stdin.readline

def find_regions(x, y, a, b):
    if x < a:
        if y < b:
            return 2

        return 1

    else:
        if y < b:
            return 3

        return 0


n = int(input())
ux, uy = set(), set()
locations = []
for _ in range(n):
    x, y = map(int, input().split())
    ux.add(x)
    uy.add(y)
    locations.append((x, y))

ux = sorted(ux)
uy = sorted(uy)

matrix = [[0] * n for _ in range(n)]
xarr, yarr = [], []
for x, y in locations:
    xarr.append(ux.index(x))
    yarr.append(uy.index(y))
    matrix[xarr[-1]][yarr[-1]] += 1
sum_matrix = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if (x, y) == (0, 0):
            sum_matrix[x][y] = matrix[x][y]

        elif not x:
            sum_matrix[x][y] = sum_matrix[x][y - 1] + matrix[x][y]

        elif not y:
            sum_matrix[x][y] = sum_matrix[x - 1][y] + matrix[x][y]

        else:
            sum_matrix[x][y] = sum_matrix[x - 1][y] + sum_matrix[x][y - 1] - sum_matrix[x - 1][y - 1] + matrix[x][y]

m = n
for x in range(n):
    for y in range(n):
        m = min(m,
                max(
                    sum_matrix[x][n - 1] - sum_matrix[x][y], # 1사분면
                    sum_matrix[x][y], # 2사분면
                    sum_matrix[n - 1][y] - sum_matrix[x][y], # 3사분면
                    sum_matrix[n - 1][n - 1] - sum_matrix[n - 1][y] - sum_matrix[x][n - 1] + sum_matrix[x][y] # 4사분면
                    )
                )

print(m)
