import sys
input = sys.stdin.readline

n = int(input())
poles = [tuple(map(int, input().split())) for _ in range(n)]
poles.sort()

result = 0
stack = []

for x, h in poles:
    if not stack:
        stack.append((x, h))
        continue

    if h > stack[-1][1]:
        result += (x - stack[-1][0]) * stack[-1][1]
        stack.append((x, h))

left = stack[-1][0]

poles.sort(reverse=True)
stack = []
for x, h in poles:
    if not stack:
        stack.append((x, h))
        continue

    if h > stack[-1][1]:
        result += (stack[-1][0] - x) * stack[-1][1]
        stack.append((x, h))

right = stack[-1][0]
result += (right - left + 1) * stack[-1][1]
print(result)
