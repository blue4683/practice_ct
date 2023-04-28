import sys,heapq
input=sys.stdin.readline
INF=21e8

def dijkstra(start):
    heapq.heappush(heap,(0,start))
    while heap:
        now_cost,now=heapq.heappop(heap)
        if now_cost>result[now]: continue
        for next_cost,next in graph[now]:
            cost=now_cost+next_cost
            if cost<result[next]:
                result[next]=cost
                heapq.heappush(heap,(cost,next))

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    start,end,cost=map(int,input().split())
    graph[start].append((cost,end))
start,end=map(int,input().split())
result=[INF]*(n+1)
result[start]=0
heap=[]
dijkstra(start)
print(result[end])