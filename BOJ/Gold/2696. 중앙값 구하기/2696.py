from heapq import *
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    arr = []
    for _ in range(m // 10 + 1):
        arr += list(map(int, input().split()))

    heap = []
    result = []
    for i in range(m):
        heappush(heap, arr[i])
        if i % 2 == 0:
            tmp = heap[:]
            for _ in range(i // 2 + 1):
                middle = heappop(tmp)

            result.append(middle)

    n = len(result)
    print(n)
    for i in range(n // 10 + 1):
        print(*result[i * 10: (i + 1) * 10])
