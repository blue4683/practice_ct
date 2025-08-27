import sys
input = sys.stdin.readline


def check(m):
    cnt = 0
    tmp = 0
    for i in range(n):
        tmp += arr[i]
        if tmp >= m:
            tmp = 0
            cnt += 1

    return 0 if cnt < k else 1


n, k = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, sum(arr)
while l <= r:
    m = (l + r) // 2
    if check(m):
        l = m + 1

    else:
        r = m - 1

print(r)
