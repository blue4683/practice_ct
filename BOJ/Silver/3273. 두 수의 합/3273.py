import sys
input = sys.stdin.readline


n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

result = 0
l, r = 0, n - 1
while l < r:
    if arr[l] + arr[r] > x:
        r -= 1

    elif arr[l] + arr[r] < x:
        l += 1

    else:
        result += 1
        l += 1

print(result)
