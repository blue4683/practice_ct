from heapq import heappush, heappop


n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if not x:
        print(0) if not heap else print(-heappop(heap))
        
    else:
        heappush(heap, -x)
        