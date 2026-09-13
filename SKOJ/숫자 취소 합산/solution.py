k = int(input())
stack = []
for _ in range(k):
    num = int(input())
    if not num:
        stack.pop()
        
    else:
        stack.append(num)
        
print(sum(stack))
