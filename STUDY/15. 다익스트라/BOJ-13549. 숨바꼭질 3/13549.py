from heapq import *
LIMIT=int(10e5)+1
INF=21e8

def hide_and_seek(n):
    heap=[[0,n]]
    while heap:
        cost,x=heappop(heap)
        for dx in [2,1,-1]:
            if dx!=2:
                xx=x+dx
                next_cost=cost+1
            else:
                xx=x*dx
                next_cost=cost
            if 0<=xx<LIMIT and next_cost<arr[xx]:
                arr[xx]=next_cost
                if xx==k: return next_cost
                heappush(heap,[next_cost,xx])

n,k=map(int,input().split())
arr=[INF]*LIMIT
arr[n]=0
print(hide_and_seek(n))