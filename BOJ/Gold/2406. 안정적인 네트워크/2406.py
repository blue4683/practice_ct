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


n, m = map(int, input().split())
graph = [i for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    if find(x) != find(y):
        union(x, y)

arr = [list(map(int, input().split())) for _ in range(n)]
edges = [(arr[y][x], y + 1, x + 1)
         for y in range(1, n) for x in range(y + 1, n)]
edges.sort()

costs, connected = 0, []
for cost, x, y in edges:
    if find(x) != find(y):
        union(x, y)
        connected.append((x, y))
        costs += cost

print(costs, len(connected))
for edge in connected:
    print(*edge)
