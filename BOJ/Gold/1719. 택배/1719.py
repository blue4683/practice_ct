import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
result = [[j + 1 for j in range(n)] for _ in range(n)]

for i in range(1, n + 1):
    graph[i][i] = 0
    result[i - 1][i - 1] = '-'


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                result[i - 1][j - 1] = result[i - 1][k - 1]

for res in result:
    print(*res)
