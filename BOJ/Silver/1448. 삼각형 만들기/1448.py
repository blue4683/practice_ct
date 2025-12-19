import sys
input = sys.stdin.readline


n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)

result = -1
for i in range(n - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        result = arr[i] + arr[i + 1] + arr[i + 2]
        break

print(result)
