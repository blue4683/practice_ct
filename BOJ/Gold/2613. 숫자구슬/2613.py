import sys
input = sys.stdin.readline


def check(k):
    result = []
    tmp = 0
    cnt = 0
    for i in range(n):
        if tmp + arr[i] > k:
            result.append(cnt)
            cnt = 1
            tmp = arr[i]

        else:
            tmp += arr[i]
            cnt += 1

    if tmp > 0:
        result.append(cnt)

    return result


n, m = map(int, input().split())
arr = list(map(int, input().split()))
MAX = max(arr)

result = []
l, r = 0, sum(arr)
while l <= r:
    mid = (l + r) // 2
    group = check(mid)
    if len(group) <= m and max(arr) <= mid:
        result = group[:]
        r = mid - 1

    else:
        l = mid + 1

print(l)
while len(result) < m:
    for i in range(len(result)):
        if result[i] > 1:
            tmp = result[i]
            del result[i]
            result.insert(i, tmp // 2 + tmp % 2)
            result.insert(i, tmp // 2)
            if len(result) == m:
                break

print(*result)
