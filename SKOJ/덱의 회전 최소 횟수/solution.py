from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
targets = list(map(int, input().split()))

result = 0
for target in targets:
    idx = q.index(target)
    if not idx:
        q.popleft()
        continue
    
    while 1:
        if q[0] == target:
            q.popleft()
            break
        
        if idx < len(q) - idx:
            while q[0] != target:
                q.append(q.popleft())
                result += 1
            
        else:
            while q[0] != target:
                q.appendleft(q.pop())
                result += 1
            
print(result)
