from heapq import *
import sys
input=sys.stdin.readline

n=int(input())
heap=[]
for x in [int(input()) for _ in range(n)]:
    if x: heappush(heap,(abs(x),x))
    else:
        if heap: print(heappop(heap)[1])
        else: print(0)