from heapq import *
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    heap = []
    for file in map(int, input().split()):
        heappush(heap, file)

    result = 0
    while len(heap) > 1:
        tmp = heappop(heap) + heappop(heap)
        result += tmp
        heappush(heap, tmp)

    print(result)
