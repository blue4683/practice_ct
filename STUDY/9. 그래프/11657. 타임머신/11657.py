import sys
input=sys.stdin.readline
INF=21e8

def bellmanFord(start):
    result[start]=0
    for i in range(n):
        for now,next,cost in edges:
            if result[now]!=INF and result[now]+cost<result[next]:
                result[next]=result[now]+cost
                if i==n-1:
                    return False
    return True

n,m=map(int,input().split())
edges=[]
result=[INF]*(n+1)
for _ in range(m):
    edges.append(list(map(int,input().split())))
if bellmanFord(1):
    for i in range(2,n+1):
        print(-1) if result[i]==INF else print(result[i])
else:
    print(-1)