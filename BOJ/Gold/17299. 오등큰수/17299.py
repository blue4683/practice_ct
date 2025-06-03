import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = [0] * (max(arr) + 1)
for num in arr:
    cnt[num] += 1

stack = []
result = [-1] * n
for i in range(n - 1, -1, -1):
    while stack and cnt[arr[i]] >= cnt[stack[-1]]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(arr[i])

print(*result)
