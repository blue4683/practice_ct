import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if left:
            right.append(left.pop())

    elif command[0] == 'D':
        if right:
            left.append(right.pop())

    elif command[0] == 'B':
        if left:
            left.pop()

    else:
        left.append(command[1])

result = left + right[::-1]
print(''.join(result))
