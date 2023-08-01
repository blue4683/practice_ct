from heapq import *
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
heap=sorted(list(map(int,input().split())))

while m:
    m-=1
    a=heappop(heap)
    b=heappop(heap)
    for _ in range(2): heappush(heap,a+b)

print(sum(heap))