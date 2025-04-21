import sys
input = sys.stdin.readline
INF = 10 ** 9


def get_path(s, e):
    if path[s][e] == -1:
        print(0)
        return

    p = [e]
    while path[s][e] != -1:
        e = path[s][e]
        p.append(e)

    print(len(p), *reversed(p))
    return


n, m = int(input()), int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
path = [[-1] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    path[a][b] = a

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]
                path[start][end] = path[mid][end]

for y in range(1, n + 1):
    for x in range(1, n + 1):
        if graph[y][x] == INF:
            graph[y][x] = 0

for l in graph[1:]:
    print(*l[1:])

for y in range(1, n + 1):
    for x in range(1, n + 1):
        get_path(y, x)
