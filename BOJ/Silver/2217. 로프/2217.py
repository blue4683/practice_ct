import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)

result = arr[0]
for i in range(1, n):
    result = max(result, arr[i] * (i + 1))

print(result)
