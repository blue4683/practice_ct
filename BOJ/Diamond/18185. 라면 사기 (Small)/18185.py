import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) + [0] * 2
result = 0

for i in range(n):
    if arr[i + 1] > arr[i + 2]:
        cnt = min(arr[i], arr[i + 1] - arr[i + 2])
        result += cnt * 5
        for j in range(2):
            arr[i + j] -= cnt

        cnt = min(arr[i], min(arr[i + 1], arr[i + 2]))
        result += cnt * 7
        for j in range(3):
            arr[i + j] -= cnt

    else:
        cnt = min(arr[i], min(arr[i + 1], arr[i + 2]))
        result += cnt * 7
        for j in range(3):
            arr[i + j] -= cnt

        cnt = min(arr[i], arr[i + 1])
        result += cnt * 5
        for j in range(2):
            arr[i + j] -= cnt

    result += arr[i] * 3

print(result)
