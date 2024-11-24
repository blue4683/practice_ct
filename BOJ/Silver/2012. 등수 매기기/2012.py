import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()

result = 0
for i in range(n):
    result += abs(i - arr[i] + 1)

print(result)
