import sys
input = sys.stdin.readline

n = int(input())
now = list(map(int, input().split()))
target = list(map(int, input().split()))
required = list(map(lambda x, y: y - x, now, target))

result = 0
start = 0
while 1:
    if required[start] > 0:
        result += 1
        for i in range(start, n):
            if required[i] <= 0:
                break

            required[i] -= 1

    elif required[start] < 0:
        result += 1
        for i in range(start, n):
            if required[i] >= 0:
                break

            required[i] += 1

    for i in range(start, n):
        if required[i]:
            start = i
            break

    else:
        break

print(result)
