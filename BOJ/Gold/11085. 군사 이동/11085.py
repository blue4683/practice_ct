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


p, w = map(int, input().split())
c, v = map(int, input().split())

graph = [i for i in range(p)]
edges = []
for _ in range(w):
    s, e, width = map(int, input().split())
    edges.append((width, s, e))

edges.sort(reverse=True)
result = 10 ** 9
for width, s, e in edges:
    if find(s) != find(e):
        union(s, e)
        result = min(result, width)

    if find(c) == find(v):
        break

print(result)
