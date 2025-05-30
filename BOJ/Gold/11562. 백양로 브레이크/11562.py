import sys
input = sys.stdin.readline
INF = 10 ** 9


def floyd(graph):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph


n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    u, v, b = map(int, input().split())
    graph[u][v] = 0
    graph[v][u] = b ^ 1

graph = floyd(graph)
for _ in range(int(input())):
    u, v = map(int, input().split())
    print(graph[u][v])
