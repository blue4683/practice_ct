import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    tmp = [value - mid if value - mid < 0 else 0 for value in arr]
    if mid * n + sum(tmp) <= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)