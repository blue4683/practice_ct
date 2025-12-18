import sys
input = sys.stdin.readline


n = int(input())

result = 0
r = len(str(n)) - 1
while 1:
    if r:
        result += (r + 1) * ((n - (10 ** r)) + 1)

    else:
        result += n

    n = 10 ** r - 1
    if not r:
        break

    r -= 1

print(result)
