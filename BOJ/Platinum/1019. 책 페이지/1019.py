import sys
input = sys.stdin.readline

n = input().rstrip()
m = len(n)
exp = [10 ** i for i in range(m + 1)]

result = [0] * 10
for num in n:
    m -= 1
    for i in range(int(num)):
        result[i] += 10 ** m
        for j in range(10):
            if m >= 1:
                result[j] += m * exp[m - 1]

    result[0] -= 10 ** m
    result[int(num)] += int(n[-m:]) + 1 if m else 1

print(*result)
