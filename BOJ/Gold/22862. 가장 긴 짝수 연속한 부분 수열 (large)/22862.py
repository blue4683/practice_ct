import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(lambda x: int(x) % 2, input().split()))
cnt = arr[0]
left, right = 0, 0
result = 0

while left < n:
    if cnt <= k:
        result = max(result, right - left + 1 - cnt)
        if right < n - 1:
            right += 1
            cnt += arr[right]

        else:
            break

    else:
        cnt -= arr[left]
        left += 1

print(result)
