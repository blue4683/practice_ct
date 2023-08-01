from heapq import *
import sys
input=sys.stdin.readline

n=int(input())
heap,max_day=[],0
for _ in range(n):
    d,w=map(int,input().split())
    if d>max_day: max_day=d
    heappush(heap,(-w,d))

visited=[0]*(max_day+1)

while heap:
    score,day=heappop(heap)
    while 1:
        if day<1: break
        if visited[day]==0:
            visited[day]-=score
            break
        day-=1

print(sum(visited))