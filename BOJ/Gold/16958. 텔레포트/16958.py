import sys
input = sys.stdin.readline
INF = 10 ** 9


n, t = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

cities = [tuple(map(int, input().split())) for _ in range(n)]
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        _, x1, y1, _, x2, y2 = *cities[a - 1], *cities[b - 1]
        dist = abs(x1 - x2) + abs(y1 - y2)
        if cities[a - 1][0] and cities[b - 1][0]:
            graph[a][b] = dist if dist < t else t
            graph[b][a] = dist if dist < t else t

        else:
            graph[a][b] = dist
            graph[b][a] = dist

for mid in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if graph[s][mid] + graph[mid][e] < graph[s][e]:
                graph[s][e] = graph[s][mid] + graph[mid][e]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(graph[a][b])
