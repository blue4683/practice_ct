import sys
input = sys.stdin.readline
INF = 10 ** 9

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for a, b, c in [list(map(int, input().split())) for _ in range(e)]:
    graph[a][b] = min(graph[a][b], c)

for mid in range(1, v + 1):
    for start in range(1, v + 1):
        for end in range(1, v + 1):
            graph[start][end] = min(
                graph[start][end], graph[start][mid] + graph[mid][end])

result = min([graph[i][i] for i in range(1, v + 1)])
print(result) if result != INF else print(-1)
