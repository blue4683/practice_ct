from heapq import *
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

jewels = sorted([list(map(int, input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])

result = 0
available_jewels = []

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        _, value = heappop(jewels)
        heappush(available_jewels, -value)

    if available_jewels:
        result -= heappop(available_jewels)

print(result)
