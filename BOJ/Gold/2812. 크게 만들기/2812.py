import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = input().rstrip()
stack = []

for num in number:
    while stack and k and int(stack[-1]) < int(num):
        k -= 1
        stack.pop()

    stack.append(num)

if k:
    stack = stack[:-k]

number = ''.join(stack)
print(number)
