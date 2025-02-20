import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

liquid = 3 * (10 ** 9) + 1
result = (0, 0, 0)
for i in range(n):
    l = i + 1
    r = n - 1
    while l < r:
        tmp = arr[l] + arr[r]
        if abs(tmp + arr[i]) < abs(liquid):
            liquid = tmp + arr[i]
            result = (arr[i], arr[l], arr[r])

        if tmp + arr[i] > 0:
            r -= 1

        elif tmp + arr[i] < 0:
            l += 1

        else:
            break

print(*result)
