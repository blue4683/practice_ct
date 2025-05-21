import sys
input = sys.stdin.readline


def is_possible(mid):
    cnt = 0
    s = 0
    i = 1
    while s + i <= n:
        if max(arr[s:s + i]) - min(arr[s:s + i]) <= mid:
            i += 1
            continue

        else:
            cnt += 1
            s = s + i - 1
            i = 1

    return 0 if cnt + 1 > m else 1


n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
l, r = 0, 10000
while l <= r:
    mid = (l + r) // 2
    if is_possible(mid):
        r = mid - 1
        result = mid

    else:
        l = mid + 1

print(result)
