import sys
input = sys.stdin.readline
INF = 10 ** 9


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

graph = [[1 if arr[y][x] == 'Y' else INF for x in range(n)] for y in range(n)]
for i in range(n):
    graph[i][i] = 0

for mid in range(n):
    for s in range(n):
        for e in range(n):
            if graph[s][e] > graph[s][mid] + graph[mid][e]:
                graph[s][e] = graph[s][mid] + graph[mid][e]

for y in range(n):
    for x in range(n):
        graph[x][y] = 1 if x != y and 0 < graph[x][y] <= 2 else 0

print(max(map(sum, graph)))
