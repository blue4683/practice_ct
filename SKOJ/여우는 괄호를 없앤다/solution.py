s = input().rstrip()

pairs = {'(': ')', '[': ']', '{': '}'}
stack = []
max_depth = 0

for ch in s:
    if stack and pairs.get(stack[-1]) == ch:
        max_depth = max(max_depth, len(stack))
        stack.pop()
        
    else:
        stack.append(ch)

print(max_depth if not stack else -1)
