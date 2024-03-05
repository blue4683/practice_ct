import sys
input = sys.stdin.readline


def gcd(a, b):
    if not b:
        return a

    return gcd(b, a % b)


def factorial(n):
    cnt = 1
    for i in range(1, n + 1):
        cnt *= i

    return cnt


n = int(input())
numbers = [int(input()) for _ in range(n)]
k = int(input())

dp = [[0] * 101 for _ in range(1 << n)]
dp[0][0] = 1

length = [len(str(number)) for number in numbers]
a = [0] * n
for i in range(n):
    for j in range(length[i]):
        a[i] = (a[i] * 10 + int(str(numbers[i])[j])) % k

ten = [10 ** i % k for i in range(51)]

for bit in range(1 << n):
    for i in range(k):
        for j in range(n):
            if bit & (1 << j) == 0:
                next = (((i * ten[length[j]]) % k) + a[j]) % k
                dp[bit | (1 << j)][next] += dp[bit][i]

p = dp[(1 << n) - 1][0]
q = factorial(n)
g = gcd(p, q)

print(f'{p//g}/{q//g}') if p else print(f'{0}/{1}')
