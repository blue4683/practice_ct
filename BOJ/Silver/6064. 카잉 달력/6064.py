import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    a, b = x, y
    result = -1
    for _ in range(m + n):
        if a > b:
            b += n

        elif a < b:
            a += m

        else:
            result = a
            break

    print(result)
