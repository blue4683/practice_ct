import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr = list(set(arr))
n = len(arr)
arr.sort()

left, right = 0, 0
result = 2 * 10 ** 9
while left < n:
    diff = arr[right] - arr[left]
    if diff < m:
        if right < n - 1:
            right += 1

        else:
            left += 1

    else:
        result = min(result, diff)
        left += 1

print(result)
