from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
stack, heap = [], []
for _ in range(n):
    heappush(heap, list(map(int, input().split())))

end = 0
while heap:
    l, h, r = heappop(heap)
    if l >= end:
        if l > end:
            stack.append((end, 0))
            stack.append((l, h))

        else:
            if h != stack[-1][1]:
                stack.append((l, h))

        end = r
        continue

    if h <= stack[-1][1]:
        if r > end:
            heappush(heap, [end, h, r])

        continue

    if end > r:
        heappush(heap, [r, stack[-1][1], end])

    if l == stack[-1][0]:
        stack.pop()

    stack.append((l, h))
    end = r

stack.append((end, 0))
for pos in stack[1:]:
    print(*pos, end=" ")
