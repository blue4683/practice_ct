import sys, heapq
input=sys.stdin.readline
INF=int(21e8)

def dijkstra(start):
    heapq.heappush(heap,(0,start))
    while heap:
        now_cost,now=heapq.heappop(heap)
        if result[now]<now_cost: continue
        for next,next_cost in graph[now]:
            cost=now_cost+next_cost
            if cost<result[next]:
                result[next]=cost
                heapq.heappush(heap,(cost,next))

v,e=map(int,input().split())
start=int(input())
graph=[[] for _ in range((v+1))]
for _ in range(e):
    s,e,cost=map(int,input().split())
    graph[s].append((e,cost))
result=[INF]*(v+1)
result[start]=0
heap=[]

dijkstra(start)
for res in result[1:]:
    print('INF') if res==INF else print(res)