from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
stations = [tuple(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())
stations.sort()

stations.append((l, 0))
result = 0
now = 0
heap = []

for pos, fuel in stations:
    dist = pos - now
    while heap and dist > p:
        result += 1
        p -= heappop(heap)

    p -= dist
    if p < 0:
        result = -1
        break

    now = pos
    heappush(heap, -fuel)

print(result)
