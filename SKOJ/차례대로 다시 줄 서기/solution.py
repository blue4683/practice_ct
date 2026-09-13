from collections import deque


n, q = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
for _ in range(q):
    command = input().rstrip()
    if command == 'OUT':
        queue.popleft()
        
    else:
        queue.append(queue.popleft())
        
print(*queue) if queue else print('EMPTY')

