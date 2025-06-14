from itertools import combinations
import sys
input = sys.stdin.readline

while 1:
    k, *arr = list(map(int, input().split()))
    if not k:
        break

    for comb in combinations(arr, 6):
        print(*comb)

    print()
