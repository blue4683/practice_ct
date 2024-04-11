import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sqr = [0] * n
two = 1

for i in range(n):
    sqr[i] = two - 1
    two *= 2
    two %= MOD

result = 0

for i in range(n):
    result = (result + arr[n - 1 - i] * sqr[n - 1 - i]) % MOD
    result = (result - arr[i] * sqr[n - 1 - i]) % MOD

print(result)
