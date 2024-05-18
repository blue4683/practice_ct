import sys
input = sys.stdin.readline

while 1:
    n, *arr = list(map(int, input().split()))
    if not n:
        break

    stack = []
    result = 0

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            h = arr[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            result = max(result, w * h)

        stack.append(i)

    while stack:
        h = arr[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        result = max(result, w * h)

    print(result)
