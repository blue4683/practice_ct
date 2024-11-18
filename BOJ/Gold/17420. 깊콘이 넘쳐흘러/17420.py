import math
import sys
input = sys.stdin.readline

n = int(input())
deadline = list(map(int, input().split()))
date = list(map(int, input().split()))
gifticon = [[date[i], deadline[i]] for i in range(n)]
gifticon.sort()

before = gifticon[0][0]
day = 0
result = 0
for i in range(n):
    b, a = gifticon[i]
    if before > a:
        before = max(before, b)
        cnt = math.ceil((before - a) / 30)
        a += cnt * 30
        result += cnt

    day = max(day, a)
    if i + 1 < n and b != gifticon[i + 1][0]:
        before = day

print(result)
