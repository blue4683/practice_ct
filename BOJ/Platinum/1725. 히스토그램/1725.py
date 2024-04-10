import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for _ in range(n)]

result = 0
stack = []

for i in range(n):
    while stack and graph[stack[-1]] > graph[i]:
        h = graph[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        result = max(result, h * w)

    stack.append(i)

while stack:
    h = graph[stack.pop()]
    w = n if not stack else n - stack[-1] - 1
    result = max(result, h * w)

print(result)
