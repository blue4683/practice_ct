import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = 0

for _ in range(n):
    height = int(input())
    same = 1
    while stack and stack[-1][0] < height:
        result += stack[-1][1]
        stack.pop()

    if stack:
        if stack[-1][0] == height:
            result += stack[-1][1]
            same = stack[-1][1] + 1
            if len(stack) > 1:
                result += 1

            stack.pop()

        else:
            result += 1

    stack.append([height, same])

print(result)
