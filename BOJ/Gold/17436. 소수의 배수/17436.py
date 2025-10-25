from itertools import combinations
import math
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(1, n + 1):
    combination = combinations(arr, i)
    for comb in combination:
        k = math.prod(comb)
        v = m // k
        if i % 2:
            result += v

        else:
            result -= v

print(result)
