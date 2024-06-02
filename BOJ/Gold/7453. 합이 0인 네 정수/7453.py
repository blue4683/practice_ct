import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

left_arr, right_arr = [], []
for i in range(n):
    for j in range(n):
        left_arr.append(arr[i][0] + arr[j][1])
        right_arr.append(arr[i][2] + arr[j][3])

left_arr.sort()
right_arr.sort()

l, r = 0, n ** 2 - 1
result = 0

while l < n ** 2 and r >= 0:
    diff = left_arr[l] + right_arr[r]
    if diff < 0:
        l += 1

    elif diff > 0:
        r -= 1

    else:
        lcnt, rcnt = 1, 1
        while l + 1 < n ** 2 and left_arr[l] == left_arr[l + 1]:
            lcnt += 1
            l += 1

        while r > 0 and right_arr[r] == right_arr[r - 1]:
            rcnt += 1
            r -= 1

        result += lcnt * rcnt
        l += 1

print(result)
