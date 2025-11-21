import sys
input = sys.stdin.readline


n = int(input())
l, r = 1, n
while l <= r:
    mid = (l + r) // 2
    if n // mid < mid:
        r = mid - 1

    else:
        l = mid + 1

print(r)
