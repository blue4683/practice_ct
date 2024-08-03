import sys
input = sys.stdin.readline

n = int(input())
buildings = tuple(map(int, input().split()))

result = [[0, 0] for _ in range(n)]
stack = [(0, 1000000)]
for i in range(n):
    while stack and buildings[i] >= stack[-1][0]:
        stack.pop()

    if stack:
        result[i][0] += len(stack)
        result[i][1] = stack[-1][1]

    stack.append((buildings[i], i + 1))

stack = [(0, 1000000)]
for i in range(n - 1, -1, -1):
    while stack and buildings[i] >= stack[-1][0]:
        stack.pop()

    if stack:
        result[i][0] += len(stack)
        if not result[i][1] or abs(i + 1 - result[i][1]) > abs(i + 1 - stack[-1][1]):
            result[i][1] = stack[-1][1]

    stack.append((buildings[i], i + 1))


for res in result:
    print(*res) if res != [0, 0] else print(0)
