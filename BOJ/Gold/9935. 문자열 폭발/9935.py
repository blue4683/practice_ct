import sys
input = sys.stdin.readline

word = input().rstrip()
explosive = input().rstrip()
stack = []

for i in range(len(word)):
    stack.append(word[i])
    if len(stack) >= len(explosive):
        if ''.join(stack[-len(explosive):]) == explosive:
            for _ in range(len(explosive)):
                stack.pop()

result = ''.join(stack)
print(result) if result else print('FRULA')
