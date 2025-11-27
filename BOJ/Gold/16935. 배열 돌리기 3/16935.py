import sys
input = sys.stdin.readline


def process(num, arr):
    global n, m
    if num == 1:
        for y in range(n // 2):
            arr[y], arr[n - 1 - y] = arr[n - 1 - y][:], arr[y][:]

        return arr

    if num == 2:
        for y in range(n):
            arr[y] = arr[y][::-1]

        return arr

    if num == 3:
        tmp = [[0] * n for _ in range(m)]
        for y in range(n):
            for x in range(m):
                tmp[x][n - 1 - y] = arr[y][x]

        n, m = m, n
        return tmp

    if num == 4:
        tmp = [[0] * n for _ in range(m)]
        for y in range(n):
            for x in range(m):
                tmp[m - 1 - x][y] = arr[y][x]

        n, m = m, n
        return tmp

    if num == 5:
        tmp = [[0] * m for _ in range(n)]
        for y in range(n):
            for x in range(m):
                if y < n // 2 and x < m // 2:
                    tmp[y][x + m // 2] = arr[y][x]

                elif y < n // 2 and x >= m // 2:
                    tmp[y + n // 2][x] = arr[y][x]

                elif y >= n // 2 and x >= m // 2:
                    tmp[y][x - m // 2] = arr[y][x]

                else:
                    tmp[y - n // 2][x] = arr[y][x]

        return tmp

    else:
        tmp = [[0] * m for _ in range(n)]
        for y in range(n):
            for x in range(m):
                if y < n // 2 and x < m // 2:
                    tmp[y + n // 2][x] = arr[y][x]

                elif y < n // 2 and x >= m // 2:
                    tmp[y][x - m // 2] = arr[y][x]

                elif y >= n // 2 and x >= m // 2:
                    tmp[y - n // 2][x] = arr[y][x]

                else:
                    tmp[y][x + m // 2] = arr[y][x]

        return tmp


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in map(int, input().split()):
    arr = process(i, arr)

for l in arr:
    print(*l)
