import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

for mid in range(n):
    for start in range(n):
        for end in range(n):
            if graph[start][end]: continue
            if graph[start][mid] and graph[mid][end]:
                graph[start][end]=1

for line in graph:
    print(*line)