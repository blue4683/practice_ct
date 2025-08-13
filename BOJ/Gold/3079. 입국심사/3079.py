import sys
input = sys.stdin.readline


def check(k):
    cnt = 0
    for i in range(n):
        cnt += k // arr[i]
        if cnt >= m:
            return 1

    return 0


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
l, r = 1, max(arr) * m
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1

    else:
        l = mid + 1

print(l)
