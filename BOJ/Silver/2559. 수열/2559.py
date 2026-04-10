import sys
input = sys.stdin.readline


n, k = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr[:k])
result = total
for i in range(k, n):
    total = total - arr[i - k] + arr[i]
    result = max(result, total)

print(result)
