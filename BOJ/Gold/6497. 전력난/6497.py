import sys
input = sys.stdin.readline


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


while 1:
    m, n = map(int, input().split())
    if not (m or n):
        break

    edges = []
    result = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        result += z
        edges.append((z, x, y))

    edges.sort()
    graph = [i for i in range(m)]

    for cost, x, y in edges:
        if find(x) == find(y):
            continue

        union(x, y)
        result -= cost

    print(result)
