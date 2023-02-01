import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    o = int(input())
    if o == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, o)