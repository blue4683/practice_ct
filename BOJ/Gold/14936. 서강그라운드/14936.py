import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            graph[start][end] = min(
                graph[start][end], graph[start][mid] + graph[mid][end])

result = 0
for y in range(1, n + 1):
    tmp = 0
    for x in range(1, n + 1):
        if graph[y][x] <= m:
            tmp += items[x]

    result = max(result, tmp)

print(result)
