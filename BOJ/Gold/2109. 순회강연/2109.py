from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[-1])
heap = []

for i in range(n):
    p, d = arr[i]
    heappush(heap, p)
    if len(heap) > d:
        heappop(heap)

print(sum(heap))
