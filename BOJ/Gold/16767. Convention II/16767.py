from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(1, n + 1):
    a, t = map(int, input().split())
    heappush(heap, (a, i, t))

wait = []
result = 0
time = 0
while heap or wait:
    while heap and time > heap[0][0]:
        a, i, t = heappop(heap)
        heappush(wait, (i, a, t))

    if not wait:
        a, i, t = heappop(heap)
        time = a + t

    else:
        i, a, t = heappop(wait)
        result = max(result, time - a)
        time += t

print(result)
