from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    a, b = arr[x // c][x % c], arr[y // c][y % c]
    if a > b:
        graph[x] = y

    else:
        graph[y] = x


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

graph = [i for i in range(r * c)]
for y in range(r):
    for x in range(c):
        v, fy, fx = arr[y][x], y, x
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or v < arr[yy][xx]:
                continue

            v, fy, fx = arr[yy][xx], yy, xx

        if v == arr[y][x]:
            continue

        union(c * y + x, c * fy + fx)

result = [[0] * c for _ in range(r)]

for i in range(r * c):
    n = find(graph[i])
    result[n // c][n % c] += 1

for res in result:
    print(*res)
