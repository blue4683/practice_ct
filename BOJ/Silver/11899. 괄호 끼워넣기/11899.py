import sys
input = sys.stdin.readline


arr = input().rstrip()
stack = []
for s in arr:
    if stack and stack[-1] == '(' and s == ')':
        stack.pop()

    else:
        stack.append(s)

print(len(stack))
