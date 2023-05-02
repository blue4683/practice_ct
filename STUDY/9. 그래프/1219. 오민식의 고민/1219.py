import sys
input=sys.stdin.readline
INF=-21e8

def bellmanFord():
    for i in range(n+101):
        for now,next,cost in edges:
            if result[now]==INF: continue
            elif result[now]==-INF: result[next]=-INF
            elif result[now]+cost>result[next]:
                result[next]=result[now]+cost
                if i>=n-1:
                    result[next]=-INF

n,start,end,m=map(int,input().split())
edges=[list(map(int,input().split())) for _ in range(m)]
earning=list(map(int,input().split()))
for i in range(m):
    edges[i][2]=earning[edges[i][1]]-edges[i][2]

result=[INF]*n
result[start]=earning[start]
bellmanFord()
if result[end]==INF: print('gg')
elif result[end]==-INF: print('Gee')
else: print(result[end])