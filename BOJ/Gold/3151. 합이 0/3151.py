import sys
input = sys.stdin.readline


n = int(input())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    if arr[i] > 0:
        break

    l, r = i + 1, n - 1
    while l < r:
        tmp = arr[l] + arr[r] + arr[i]
        if tmp == 0:
            if arr[l] == arr[r]:
                k = r - l + 1
                result += (k * (k - 1)) // 2
                break

            lcnt, rcnt = 1, 1
            while arr[l] == arr[l + 1]:
                lcnt += 1
                l += 1

            while arr[r] == arr[r - 1]:
                rcnt += 1
                r -= 1

            result += lcnt * rcnt

        if tmp > 0:
            r -= 1

        else:
            l += 1

print(result)
