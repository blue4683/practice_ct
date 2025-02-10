import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lines = sorted([list(map(int, input().split())) for _ in range(n)])

m = max(map(lambda x: x[1], lines)) + 1
arr = [0] * m
for a, b in lines:
    for i in range(a, b):
        arr[i] += 1

result = (len(arr), len(arr))
cnt = arr[0]
left, right = 0, 1
while left < m:
    if cnt <= k:
        if cnt == k:
            result = min(result, (left, right))

        if right < m - 1:
            cnt += arr[right]
            right += 1

        else:
            break

    else:
        cnt -= arr[left]
        left += 1

print(*result) if result != (len(arr), len(arr)) else print(0, 0)
