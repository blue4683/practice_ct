import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

result = max(dp)
print(result)

nums = []
for i in range(n - 1, - 1, - 1):
    if result == 0:
        break

    if result == dp[i]:
        nums.append(arr[i])
        result -= 1

print(*reversed(nums))
