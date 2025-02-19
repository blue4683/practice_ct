from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

asum = [0] * (n + 1)
for i in range(n):
    asum[i + 1] += asum[i] + a[i]

adict = defaultdict(int)
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        adict[asum[j] - asum[i]] += 1

result = 0
for i in range(m):
    prefix = 0
    for j in range(i, m):
        prefix += b[j]
        if t - prefix in adict:
            result += adict[t - prefix]

print(result)
