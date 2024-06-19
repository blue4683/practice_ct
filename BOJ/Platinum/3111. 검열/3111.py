from collections import deque
import sys
input = sys.stdin.readline


def slicing(stack, string, target, is_back):
    while string:
        if is_back:
            stack.append(string.pop())

        else:
            stack.append(string.popleft())

        if stack[-1] == target[-1] and stack[-n:] == target:
            for _ in range(n):
                stack.pop()

            return 1

    return 0


a = list(input().rstrip())
reversed_a = list(reversed(a))
t = deque(list(input().rstrip()))

n = len(a)
front, back = [], []
while 1:
    if slicing(front, t, a, 0) and slicing(back, t, reversed_a, 1):
        continue

    break

while 1:
    if slicing(front, back, a, 1):
        continue

    break

print(''.join(front))
