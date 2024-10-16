import sys
input = sys.stdin.readline

n = int(input())
rooms = [int(input()) for _ in range(n)]
result = 10 ** 9

for pivot in range(n):
    tmp = 0
    for i in range(n):
        if pivot == i:
            continue

        elif pivot > i:
            tmp += (n - pivot + i) * rooms[i]

        else:
            tmp += (i - pivot) * rooms[i]

    result = min(result, tmp)

print(result)
