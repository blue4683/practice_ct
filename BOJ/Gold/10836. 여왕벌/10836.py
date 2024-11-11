import sys
input = sys.stdin.readline


m, n = map(int, input().split())
hive = [[1] * m for _ in range(m)]
growth = [0] * (2 * m - 1)
for _ in range(n):
    a, b, c = map(int, input().split())
    for i in range(a, a + b):
        growth[i] += 1

    for i in range(a + b, 2 * m - 1):
        growth[i] += 2

for y in range(m):
    for x in range(m):
        if not x:
            hive[y][x] += growth[m - 1 - y]

        else:
            hive[y][x] += growth[m - 1 + x]

for arr in hive:
    print(*arr)
