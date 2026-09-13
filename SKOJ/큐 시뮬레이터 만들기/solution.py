from collections import deque


n = int(input())
q = deque()

for _ in range(n):
    params = input().split()
    if params[0] == 'push':
        q.append(int(params[1]))
        
    elif params[0] == 'pop':
        print(-1) if not q else print(q.popleft())
        
    elif params[0] == 'size':
        print(len(q))
        
    elif params[0] == 'empty':
        print(int(len(q) == 0))
        
    elif params[0] == 'front':
        print(-1) if not q else print(q[0])
        
    else:
        print(-1) if not q else print(q[-1])
        