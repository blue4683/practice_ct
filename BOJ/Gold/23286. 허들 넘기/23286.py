import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m, t = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    u, v, h = map(int, input().split())
    if graph[u][v] > h:
        graph[u][v] = h

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > max(graph[i][k], graph[k][j]):
                graph[i][j] = max(graph[i][k], graph[k][j])

graph = [list(map(lambda x: -1 if x == INF else x, line)) for line in graph]
for _ in range(t):
    s, e = map(int, input().split())
    print(graph[s][e])
