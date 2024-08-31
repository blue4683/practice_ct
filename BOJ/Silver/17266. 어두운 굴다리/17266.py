import math
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
pos = list(map(int, input().split()))
before = pos[0]
result = pos[0]

for x in pos[1:]:
    result = max(result, math.ceil((x - before) / 2))
    before = x

print(max(result, n - before))
