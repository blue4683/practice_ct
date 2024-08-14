from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    for num in map(int, input().split()):
        heappush(heap, num)
        if len(heap) > n:
            heappop(heap)

print(heappop(heap))
