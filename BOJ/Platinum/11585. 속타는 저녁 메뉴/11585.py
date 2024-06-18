import sys
input = sys.stdin.readline


def gcd(a, b):
    while 1:
        c = a % b
        if not c:
            return b

        a = b
        b = c


n = int(input())
pattern = ''.join(input().split())
string = ''.join(input().split() * 2)

table = [0] * n
i = 0
for j in range(1, n):
    while i > 0 and pattern[i] != pattern[j]:
        i = table[i - 1]

    if pattern[i] == pattern[j]:
        i += 1
        table[j] = i

result = 0
i = 0
for j in range(1, n * 2):
    while i > 0 and pattern[i] != string[j]:
        i = table[i - 1]

    if pattern[i] == string[j]:
        if i == n - 1:
            result += 1
            i = table[i]

        else:
            i += 1

mod = gcd(n, result)
print(f'{result // mod}/{n // mod}')
