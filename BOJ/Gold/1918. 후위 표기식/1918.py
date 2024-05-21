import sys
input = sys.stdin.readline


def is_alphabet(s):
    if ord('A') <= ord(s) <= ord('Z'):
        return 1

    return 0


expression = input().rstrip()
result = ''
stack = []

for s in expression:
    if is_alphabet(s):
        result += s

    elif s == '(':
        stack.append(s)

    elif s in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            result += stack.pop()

        stack.append(s)

    elif s in ['+', '-']:
        while stack and stack[-1] != '(':
            result += stack.pop()

        stack.append(s)

    else:
        while stack and stack[-1] != '(':
            result += stack.pop()

        stack.pop()

while stack:
    result += stack.pop()

print(result)
