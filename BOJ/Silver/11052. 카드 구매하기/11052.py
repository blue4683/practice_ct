import sys

input = sys.stdin.readline

n = int(input())
prices = list(map(int, input().split()))

result = [0] * (n + 1)

for i in range(n):
    price = prices[i]
    for j in range(1, n + 1):
        if j - i - 1 >= 0:
            result[j] = max(result[j], result[j - i - 1] + price)

print(result[n])
