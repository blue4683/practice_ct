import sys
input = sys.stdin.readline


def check(mid):
    global result
    cnt = 0
    for i in range(1, n + 2):
        l, r = arr[i - 1], arr[i]
        if r - l < mid:
            continue

        if (r - l) % mid:
            cnt += (r - l) // mid

        else:
            cnt += (r - l) // mid - 1

    if cnt <= m:
        result = mid
        return 1

    return 0


n, m, l = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split()))) + [l]

result = 10 ** 9
s, e = 1, l
while s <= e:
    mid = (s + e) // 2
    if check(mid):
        e = mid - 1

    else:
        s = mid + 1

print(result)
