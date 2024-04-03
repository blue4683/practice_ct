import sys
input = sys.stdin.readline


def check(arr):
    arr.sort(key=lambda x: (x[1], -x[2]))
    result = []

    for number, start, end in arr:
        if result and result[-1][2] >= end:
            continue

        result.append((number, start, end))

    return result


n = int(input())
m = int(input())
cw = []
ccw = []

for i in range(1, m + 1):
    a, b = map(int, input().split())
    if a > b:
        ccw.append((i, a, b + n))

    else:
        cw.append((i, a, b))

result1, result2 = check(cw), check(ccw)
result = []

if result2:
    result.extend([x[0] for x in result2])
    min_start = result2[0][1]
    max_end = result2[-1][-1]
    result1 = [x for x in result1 if not (
        x[1] >= min_start or x[2] <= max_end - n)]

result.extend([x[0] for x in result1])
result.sort()

print(*result)
