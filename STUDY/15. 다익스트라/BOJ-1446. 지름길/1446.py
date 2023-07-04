import sys,heapq
input=sys.stdin.readline

def find_shortcut(arr):
    while arr:
        start,end,cost=heapq.heappop(arr)
        if end<=d and road[start]+cost<road[end]:
            road[end]=road[start]+cost
            for i in range(end+1,d+1):
                if road[i]>road[end]+i-end: road[i]=road[end]+i-end

    return road[d]

n,d=map(int,input().split())
road=[i for i in range(d+1)]
heap=[]
for _ in range(n):
    heapq.heappush(heap,list(map(int,input().split())))

print(find_shortcut(heap))