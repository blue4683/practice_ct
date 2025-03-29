import sys
input = sys.stdin.readline


def get_distance(a, b):
    x1, y1, x2, y2 = *a, *b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


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


n, m = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(n)]
connected = [tuple(map(int, input().split())) for _ in range(m)]
edges = []

graph = [i for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (i, j) in connected or (j, i) in connected:
            edges.append((0, i, j))

        else:
            edges.append((get_distance(pos[i - 1], pos[j - 1]), i, j))

edges.sort()
result = 0
for dist, i, j in edges:
    if find(i) == find(j):
        continue

    result += dist
    union(i, j)

print(f'{result:.2f}')
