import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l, r = 0, n - 1

result = abs(arr[l] + arr[r])
res_l, res_r = l, r

while l < r:
    liquid = arr[l] + arr[r]
    if abs(liquid) < result:
        res_l, res_r = l, r
        result = abs(liquid)

        if result == 0:
            break

    if liquid < 0:
        l += 1

    else:
        r -= 1

print(arr[res_l], arr[res_r])
