import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
q = [int(input()) for _ in range(n)]
numList = deque([i for i in range(1, n+1)])
stack = deque([])
order = []
a = []
cur = 1
for num in q:
    while cur <= num:
        stack.append(numList.popleft())
        order.append('+')
        cur += 1
    
    if stack[-1]==num:
        a.append(stack.pop())
        order.append('-')
    else:
        print('NO')
        break
else:
    for o in order:
        print(o)