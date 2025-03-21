import sys
input = sys.stdin.readline


def is_crossed(rect1, rect2):
    x1, y1, x2, y2 = rect1
    a1, b1, a2, b2 = rect2

    if (x1 < a1 and a2 < x2 and y1 < b1 and b2 < y2):
        return 0

    if (x1 > a1 and a2 > x2 and y1 > b1 and b2 > y2):
        return 0

    if (a1 > x2 or a2 < x1 or b1 > y2 or b2 < y1):
        return 0

    return 1


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        graph[y] = x

    else:
        graph[x] = y


n = int(input())
squares = [(0, 0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

graph = [i for i in range(n + 1)]
for i in range(n + 1):
    square1 = squares[i]
    for j in range(i + 1, n + 1):
        if find(i) == find(j):
            continue

        square2 = squares[j]
        if is_crossed(square1, square2):
            union(i, j)

result = 0
check = [0] * (n + 1)
for i in range(n + 1):
    if not check[find(i)]:
        check[find(i)] = 1
        result += 1

print(result - 1)
