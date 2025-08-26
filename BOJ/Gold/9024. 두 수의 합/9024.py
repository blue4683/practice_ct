import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))

    diff = 10 ** 9
    result = 0
    l, r = 0, n - 1
    while arr[l] < arr[r]:
        tmp = abs(arr[l] + arr[r] - k)
        if tmp == diff:
            result += 1

        elif tmp < diff:
            diff = tmp
            result = 1

        if arr[l] + arr[r] <= k:
            l += 1

        else:
            r -= 1

    print(result)
