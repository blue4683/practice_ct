import sys
input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]
stack = []

result = 0
for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()

    result += len(stack)
    stack.append(building)

print(result)
