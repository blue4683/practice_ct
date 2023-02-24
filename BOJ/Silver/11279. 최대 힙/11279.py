import heapq
import sys
input=sys.stdin.readline

heap=[]
for _ in range(int(input())):
    n=int(input())
    if n:
        heapq.heappush(heap,-n)
    else:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))