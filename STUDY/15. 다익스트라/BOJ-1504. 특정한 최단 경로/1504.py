from heapq import *
import sys
input=sys.stdin.readline
INF=21e8

def find(start):
    road=[INF]*(n+1)
    road[start]=0
    heap=[]
    heappush(heap,(0,start))

    while heap:
        now_cost,now=heappop(heap)
        if road[now]<now_cost: continue
        for next,next_cost in graph[now]:
            cost=now_cost+next_cost
            if cost<road[next]:
                road[next]=cost
                heappush(heap,[cost,next])
    
    return road

n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2=map(int,input().split())

r1,r2,r3=find(1),find(v1),find(v2)

case1,case2=r1[v1]+r2[v2]+r3[n],r1[v2]+r3[v1]+r2[n]

print(-1) if case1>=INF and case2>=INF else print(min(case1,case2))