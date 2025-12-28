from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
q = deque([i for i in range(1, n + 1)])
while q:
    print(q.popleft(), end=' ')
    if q:
        q.append(q.popleft())
