import sys
input = sys.stdin.readline

arr = list(input().rstrip())
stack = []
result = 0
tmp = 1

for i in range(len(arr)):
    s = arr[i]
    if s == '(':
        tmp *= 2
        stack.append(s)

    elif s == '[':
        tmp *= 3
        stack.append(s)

    elif s == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break

        if arr[i - 1] == '(':
            result += tmp

        tmp //= 2
        stack.pop()

    elif s == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break

        if arr[i - 1] == '[':
            result += tmp

        tmp //= 3
        stack.pop()

if stack:
    result = 0

print(result)
