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
s, e = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort(key=lambda x: -x[0])
graph = [i for i in range(n + 1)]
result = 0
for k, h1, h2 in edges:
    if find(h1) != find(h2):
        union(h1, h2)

    if find(s) == find(e):
        result = k
        break

print(result)
