import sys
input = sys.stdin.readline

k = int(input())
result = [0, 0]
for i in range(21):
    if 2 ** i >= k:
        result[0] = 2 ** i
        tmp = result[0]
        for j in range(i + 1):
            if not tmp:
                break

            if k >= tmp:
                k -= tmp
                result[1] = j

            tmp //= 2

        break

print(*result)
