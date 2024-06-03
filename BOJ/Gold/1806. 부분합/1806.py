import sys
input = sys.stdin.readline
MAX = 10 ** 5 + 1

n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
prefix = arr[0]
result = MAX

while left < n:
    if prefix < s:
        if right < n - 1:
            right += 1
            prefix += arr[right]

        else:
            break

    else:
        result = min(result, right - left + 1)
        prefix -= arr[left]
        left += 1

print(result) if result != MAX else print(0)
