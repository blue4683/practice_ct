n = int(input())
target = [int(input()) for _ in range(n)]
arr = [i for i in range(n, 0, -1)]

possible = 1
result = []
stack = []
for num in target:
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
        continue
    
    if not arr or arr[-1] > num:
        possible = 0
        break
            
    while arr and arr[-1] <= num:
        stack.append(arr.pop())
        result.append('+')

    stack.pop()
    result.append('-')

if possible:
    for res in result:
        print(res)
        
else:
    print('NO')
    