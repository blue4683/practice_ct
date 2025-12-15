import sys
input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    word = input().rstrip()
    stack = []
    for alp in word:
        if not stack or stack[-1] != alp:
            stack.append(alp)

        else:
            stack.pop()

    if not stack:
        result += 1

print(result)
