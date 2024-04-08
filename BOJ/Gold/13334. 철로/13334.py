from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
rails = []
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a

    rails.append((a, b))

rails.sort()

d = int(input())
heap = []
result = 0

for right, left in rails:
    if right - left <= d:
        heappush(heap, left)

    else:
        continue

    while heap:
        start = heap[0]
        if right - start > d:
            heappop(heap)

        else:
            break

    result = max(len(heap), result)

print(result)
