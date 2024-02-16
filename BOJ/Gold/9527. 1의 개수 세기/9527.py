import sys
import math
input = sys.stdin.readline


def count_one(n):
    if n <= 0:
        return 0

    x = int(math.log2(n))
    if n == 2 ** x:
        return x * n // 2 + 1

    return count_one(2 ** x) + n - (2 ** x) + count_one(n - (2 ** x))


a, b = map(int, input().split())
print(count_one(b) - count_one(a - 1))
