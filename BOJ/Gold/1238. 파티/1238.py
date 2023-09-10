from heapq import *
import sys
input=sys.stdin.readline
INF=21e8

def dijkstra(start,end):
    result=[INF]*(n+1)
    heap=[]
    heappush(heap,[0,start])

    while heap:
        now_cost,now=heappop(heap)
        if result[now]<now_cost: continue
        for next,next_cost in graph[now]:
            cost=now_cost+next_cost
            if cost<result[next]:
                result[next]=cost
                heappush(heap,[cost,next])

    return result[end]

n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
go,back=[0]*(n+1),[0]*(n+1)
for _ in range(m):
    s,e,t=map(int,input().split())
    graph[s].append([e,t])

for i in range(1,n+1):
    if i==x: continue
    go[i]=dijkstra(i,x)
    back[i]=dijkstra(x,i)

result=[go[i]+back[i] for i in range(n+1)]
print(max(result))