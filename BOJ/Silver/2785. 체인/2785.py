from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
chains = list(map(int, input().split()))
chains.sort(reverse=True)

chain = 1
while chain + chains[-1] < n:
    chain += chains.pop()
    n -= 1

print(n - 1)
