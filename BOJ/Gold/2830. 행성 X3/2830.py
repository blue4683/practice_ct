import sys
import math
input = sys.stdin.readline
MAX = int(math.log2(10 ** 6)) + 1

n = int(input())
one, zero = [0] * MAX, [0] * MAX

for _ in range(n):
    resident = int(input())
    for i in range(MAX):
        if resident & (1 << i) != 0:
            one[i] += 1
        else:
            zero[i] += 1

value = 0

for i in range(MAX):
    value += (one[i] * zero[i]) * (2 ** i)

print(value)
