import sys
input = sys.stdin.readline


def check(m):
    if arr[0] > m:
        return 0

    cnt, over = 0, 0
    for t in arr[1:]:
        if t <= m:
            cnt += 1
            continue

        over = t // m + (t % m > 0) - 2
        if over > cnt:
            return 0

        cnt -= over

    return 1


n = int(input())
arr = sorted(list(map(int, input().split())))
l, r = arr[0], arr[-1]
while l < r:
    m = (l + r) // 2
    if check(m):
        r = m

    else:
        l = m + 1

print(r)
