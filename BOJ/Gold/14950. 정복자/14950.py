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


n, m, t = map(int, input().split())
graph = [i for i in range(n + 1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
cnt = 0
result = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cnt * t + c
        cnt += 1

print(result)
