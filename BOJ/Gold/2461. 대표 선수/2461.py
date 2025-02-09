from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
classes = []
heap = []
maxv = 0
for i in range(n):
    c = sorted(map(int, input().split()))
    maxv = max(maxv, c[0])
    heappush(heap, (c[0], i, 0))
    classes.append(c)

result = 10 ** 9
while heap:
    minv, c, i = heappop(heap)
    result = min(result, maxv - minv)
    if i == m - 1:
        break

    nextv = classes[c][i + 1]
    heappush(heap, (nextv, c, i + 1))
    maxv = max(maxv, nextv)

print(result)
