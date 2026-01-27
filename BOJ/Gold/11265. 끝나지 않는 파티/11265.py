import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for mid in range(n):
    for s in range(n):
        for e in range(n):
            if graph[s][mid] + graph[mid][e] < graph[s][e]:
                graph[s][e] = graph[s][mid] + graph[mid][e]

for _ in range(m):
    a, b, c = map(int, input().split())
    print('Enjoy other party') if graph[a -
                                        1][b - 1] <= c else print('Stay here')
