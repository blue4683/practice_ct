import sys
input = sys.stdin.readline


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = map(find, [x, y])
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


n = int(input())
ws = [list(map(int, input().split())) for _ in range(n)]

graph = [i for i in range(n)]
edges = [(y, x, ws[y][x]) for y in range(n) for x in range(y + 1, n) if y != x]
edges.sort(key=lambda x: x[-1])

result = 0
for y, x, cost in edges:
    if find(y) == find(x):
        continue

    union(y, x)
    result += cost

print(result)
