import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    pos = set(arr)
    result = 0

    for i in range(n - 1):
        x1, y1 = arr[i]
        for j in range(i + 1, n):
            x2, y2 = arr[j]
            dx, dy = x1 - x2, y1 - y2
            if (x1 - dy, y1 + dx) in pos and (x2 - dy, y2 + dx) in pos:
                result = max(result, dx ** 2 + dy ** 2)

    print(result)
