from collections import deque


n, m = map(int, input().split())
arr = deque(map(int, input().split()))

result = []
for command in input().rstrip():
    if command == 'L':
        result.append(arr.popleft())
        
    else:
        result.append(arr.pop())
        
print(*result)
