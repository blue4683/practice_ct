import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = min(graph[a][b], t)

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            graph[start][end] = min(
                graph[start][end], graph[start][mid] + graph[mid][end])

c = int(input())
nodes = list(map(int, input().split()))
dist = [0] * (n + 1)
dist[0] = INF
for i in range(1, n + 1):
    for node in nodes:
        dist[i] = max(dist[i], graph[i][node] + graph[node][i])

arr = sorted(enumerate(dist), key=lambda x: (x[1], x[0]))
minv = arr[0][1]
result = []
for i, res in arr:
    if res != minv:
        break

    result.append(i)

print(*result)
