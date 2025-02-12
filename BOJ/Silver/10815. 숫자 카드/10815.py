import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
results = []
for num in map(int, input().split()):
    result = 0
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > num:
            r = mid - 1

        elif arr[mid] < num:
            l = mid + 1

        else:
            result = 1
            break

    results.append(result)

print(*results)
