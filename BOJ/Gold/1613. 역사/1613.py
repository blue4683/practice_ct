import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 1

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if graph[s][k] + graph[k][e] == 2:
                graph[s][e] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    if graph[a][b]:
        print(-1)

    elif graph[b][a]:
        print(1)

    else:
        print(0)
