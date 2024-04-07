from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
problems = [list(map(int, input().split())) for _ in range(n)]
problems.sort()
heap = []

for deadline, count in problems:
    heappush(heap, count)
    if deadline < len(heap):
        heappop(heap)

print(sum(heap))
