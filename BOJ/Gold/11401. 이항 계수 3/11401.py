import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i % MOD

    return result


def expdiv(n, e):
    if not e:
        return 1

    elif e == 1:
        return n

    else:
        result = expdiv(n, e // 2)
        if e % 2:
            return result * result * n % MOD

        else:
            return result * result % MOD


n, k = map(int, input().split())
a = factorial(n)
b = expdiv(factorial(n - k) * factorial(k), MOD - 2)

print(a * b % MOD)
