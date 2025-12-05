import sys
input = sys.stdin.readline


def check(lst):
    result = 1
    cnt = 1
    for x in range(n - 1):
        if lst[x] == lst[x + 1]:
            cnt += 1
            result = max(result, cnt)

        else:
            cnt = 1

    return result


def swap(arr):
    result = 1
    for y in range(n):
        for x in range(n):
            if x < n - 1:
                arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x]
                result = max(result, check(arr[y]))
                arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x]

            if y < n - 1:
                arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x]
                result = max(result, check(arr[y]), check(arr[y + 1]))
                arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x]

    return result


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
tarr = list(map(list, zip(*arr)))
print(max(swap(arr), swap(tarr)))
