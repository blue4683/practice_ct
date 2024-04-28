from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
left, right = [], []
result = []
for i in range(n):
    num = int(input())
    if len(left) == len(right):
        heappush(left, (-num, num))

    else:
        heappush(right, (num, num))

    if right and left[0][1] > right[0][0]:
        min_num = heappop(right)[0]
        max_num = heappop(left)[1]
        heappush(left, (-min_num, min_num))
        heappush(right, (max_num, max_num))

    result.append(left[0][1])

for r in result:
    print(r)
