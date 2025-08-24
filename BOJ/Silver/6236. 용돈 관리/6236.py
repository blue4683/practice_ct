import sys
input = sys.stdin.readline


def check(k):
    money = k
    cnt = 1
    for i in range(n):
        if arr[i] > k:
            return 0

        if money < arr[i]:
            cnt += 1
            money = k - arr[i]

        else:
            money -= arr[i]

    return 1 if cnt <= m else 0


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
l, r = max(arr), sum(arr)
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1

    else:
        l = mid + 1

print(l)
