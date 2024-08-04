import sys
input = sys.stdin.readline


def solution():
    if a + b - 1 > n:
        return (-1, )

    result = [1] * n

    if a == 1:
        result[0] = b

    elif b == 1:
        result[-1] = a

    else:
        result[n - b] = max(a, b)

    for i in range(n - 2, n - b, -1):
        result[i] = result[i + 1] + 1

    for i in range(n - b - a + 2, n - b):
        result[i] = result[i - 1] + 1

    return result


n, a, b = map(int, input().split())
print(*solution())
