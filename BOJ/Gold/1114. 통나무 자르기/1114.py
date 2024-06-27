import sys
input = sys.stdin.readline


def cut(mid):
    between = l
    cnt = c

    for i in range(k - 1, -1, -1):
        if cnt <= 0:
            break

        if between - arr[i] > mid:
            if arr[i + 1] - arr[i] > mid:
                return - 1

            cnt -= 1
            between = arr[i + 1]

    if cnt > 0:
        between = arr[0]

    return -1 if between > mid else between


l, k, c = map(int, input().split())
arr = set(map(int, input().split()))
arr = sorted(list(arr))
arr.append(l)
k = len(arr)

start, end = l, l // (c + 1)
result = 0
while start > end:
    mid = (start + end) // 2
    result = cut(mid)

    if result >= 1:
        start = mid

    else:
        end = mid + 1

print(end, cut(end))
