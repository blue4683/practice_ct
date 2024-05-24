import sys
input = sys.stdin.readline

arr = list(input().rstrip())
stack = []
result = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])

    else:
        stack.pop()
        if arr[i - 1] == '(':
            result += len(stack)

        else:
            result += 1

print(result)
