from heapq import *
import sys
input=sys.stdin.readline

n=int(input())
classes=sorted([list(map(int,input().split())) for _ in range(n)])
heap=[]

for start,end in classes:
    if heap and heap[0]<=start: heappop(heap)
    heappush(heap,end)

print(len(heap))