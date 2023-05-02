import sys
input=sys.stdin.readline
INF=21e8

n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(c,graph[a][b])

for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            graph[start][end]=min(graph[start][end],graph[start][mid]+graph[mid][end])
for y in range(1,n+1):
    graph[y]=list(map(lambda x:0 if x==INF else x,graph[y]))

for result in graph[1:]:
    print(*result[1:])