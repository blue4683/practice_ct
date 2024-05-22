import sys
input = sys.stdin.readline


def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    op = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    if op > 0:
        return 1

    elif op == 0:
        return 0

    else:
        return -1


def is_crossed(line1, line2):
    p1, p2 = line1
    p3, p4 = line2
    x = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    y = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    if (x, y) == (0, 0):
        if p1 > p2:
            p1, p2 = p2, p1

        if p3 > p4:
            p3, p4 = p4, p3

        return p3 <= p2 and p1 <= p4

    return x <= 0 and y <= 0


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[y] = x

    else:
        graph[x] = y


n = int(input())
lines = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(((x1, y1), (x2, y2)))

graph = [i for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if is_crossed(lines[i], lines[j]):
            union(i, j)

num = [0] * n
result = 0
cnt = 0

for i in range(n):
    if graph[i] == i:
        cnt += 1

    num[find(i)] += 1
    if num[find(i)] > result:
        result = num[find(i)]

print(cnt)
print(result)
