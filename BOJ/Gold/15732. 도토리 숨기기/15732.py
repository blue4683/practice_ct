import sys
input = sys.stdin.readline


def check(mid):
    cnt = 0
    for a, b, c in arr:
        if mid < a:
            continue

        cnt += ((min(mid, b) - a) // c) + 1

    return 1 if cnt >= d else 0


n, k, d = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(k)]

l, r = 0, n
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1

    else:
        l = mid + 1

print(l)
