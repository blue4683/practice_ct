import sys
input = sys.stdin.readline

n = int(input())
pos = sorted([list(map(int, input().split())) for _ in range(n)])
stack = []
result = 0

for x, y in pos:
    while stack and stack[-1] > y:
        stack.pop()
        result += 1

    if stack and stack[-1] == y:
        continue

    stack.append(y)

while stack:
    if stack[-1] > 0:
        result += 1

    stack.pop()

print(result)
