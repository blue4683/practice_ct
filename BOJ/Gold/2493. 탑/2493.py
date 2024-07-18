import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n - 1, -1, -1):
    tower = towers[i]
    while stack and stack[-1][0] < tower:
        _, index = stack.pop()
        result[index] = i + 1

    stack.append((tower, i))

print(*result)
