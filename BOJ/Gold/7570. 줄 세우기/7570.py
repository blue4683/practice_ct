import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[arr[i]] = i

num = 1
result = 1
for i in range(1, n):
    if dp[i] < dp[i + 1]:
        num += 1
        result = max(result, num)

    else:
        num = 1

print(n - result)
