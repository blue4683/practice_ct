import sys
input = sys.stdin.readline


def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])

    return arr[x]


def union(x, y):
    x, y = find(x), find(y)
    if x >= y:
        arr[x] = y

    else:
        arr[y] = x


g = int(input())
p = int(input())
airplanes = [int(input()) for _ in range(p)]

arr = [i for i in range(g + 1)]
result = 0

for airplane in airplanes:
    if not find(airplane):
        break

    arr[airplane] -= 1
    result += 1
    union(airplane - 1, airplane)

print(result)
