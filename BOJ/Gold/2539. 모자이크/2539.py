import sys
input = sys.stdin.readline


def check(mid):
    used = set()
    for y, x in arr:
        if y > mid:
            return 0

        for xx in used:
            if abs(xx - x) < mid:
                break

        else:
            if len(used) == k:
                return 0

            used.add(x)

    return 1


n, m = map(int, input().split())
k = int(input())

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: x[-1])

result = 0
l, r = arr[-1][0], max(n, m)
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        result = mid
        r = mid - 1

    else:
        l = mid + 1

print(result)
