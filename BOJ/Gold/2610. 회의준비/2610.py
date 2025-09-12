import sys
input = sys.stdin.readline
INF = 10 ** 9


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        parent[x] = y

    else:
        parent[y] = x


n, m = int(input()), int(input())
parent = [i for i in range(n + 1)]
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    if find(a) != find(b):
        union(a, b)

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]


for i in range(n + 1):
    for j in range(n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0

group = [(max(graph[i]), i) for i in range(1, n + 1)]
group.sort()
result = []
for _, i in group:
    for j in result:
        if find(i) == find(j):
            break

    else:
        result.append(i)

result.sort()
print(len(result))
for res in result:
    print(res)
