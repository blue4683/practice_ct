import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

for mid in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if graph[s][mid] + graph[mid][e] < graph[s][e]:
                graph[s][e] = graph[s][mid] + graph[mid][e]

a, b, result = 0, 0, INF
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        dist = 0
        for mid in range(1, n + 1):
            dist += min(graph[i][mid], graph[j][mid])

        if dist < result:
            result = dist
            a, b = i, j

print(a, b, result * 2)
