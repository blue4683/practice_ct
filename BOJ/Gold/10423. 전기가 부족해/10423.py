import sys
input = sys.stdin.readline


def union(x, y):
    x, y = map(find, [x, y])
    if x in plants:
        graph[y] = x

    else:
        graph[x] = y


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


n, m, k = map(int, input().split())
plants = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[-1])

graph = [i for i in range(n + 1)]
result = 0
for x, y, cost in edges:
    xx, yy = map(find, [x, y])
    if xx == yy:
        continue

    if xx in plants and yy in plants:
        continue

    union(x, y)
    result += cost

print(result)
