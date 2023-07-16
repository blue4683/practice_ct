from heapq import *
import sys
input=sys.stdin.readline
INF=21e8

def find_cost(start,end):
    result=[INF]*(n+1)
    heap=[]
    heappush(heap,[0,start])

    while heap:
        now_cost,now=heappop(heap)
        if result[now]<now_cost: continue
        for next,next_cost in graph[now]:
            cost=next_cost+now_cost
            if cost<result[next]:
                result[next]=cost
                heappush(heap,[cost,next])

    return result[end]

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
s,t=map(int,input().split())

print(find_cost(s,t))