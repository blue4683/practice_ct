import sys,heapq
input=sys.stdin.readline
INF=21e8

def dijkstra():
    heap=[]
    heapq.heappush(heap,(0,1))
    while heap:
        now_cost,now=heapq.heappop(heap)
        for next,next_cost in graph[now]:
            cost=now_cost+next_cost
            if result[next][k-1]>cost:
                result[next][k-1]=cost
                result[next].sort()
                heapq.heappush(heap, (cost,next))

    for i in range(1,n+1):
        if result[i][-1]==INF:
            print(-1)
        else:
            print(result[i][-1])

n,m,k=map(int,input().split())
graph=[[] for _ in range(n+1)]
result=[[INF]*k for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
result[1][0]=0

dijkstra()