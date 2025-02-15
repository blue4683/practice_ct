import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

result = 0
left, right = 1, max(snacks)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for snack in snacks:
        cnt += snack // mid

    if cnt >= m:
        result = max(result, mid)
        left = mid + 1

    else:
        right = mid - 1

print(result)
