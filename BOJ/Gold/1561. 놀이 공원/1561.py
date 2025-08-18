import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))
k = max(arr)
l, r = 0, k * (n // m + 1)
while l < r:
    mid = (l + r) // 2
    cnt = sum(map(lambda x: (mid // x) + 1, arr))
    if cnt >= n:
        r = mid

    else:
        l = mid + 1

cnt = sum(map(lambda x: (l // x) + 1, arr))
result = 0
if cnt >= n:
    for i in range(m - 1, -1, -1):
        if not l % arr[i]:
            if cnt == n:
                result = i + 1
                break

            else:
                cnt -= 1

else:
    for i in range(m):
        if not (l + 1) % arr[i]:
            cnt += 1
            if cnt == n:
                result = i + 1
                break

print(result)
