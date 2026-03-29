from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

result = 0
q = deque([i for i in range(1, n + 1)])
for num in map(int, input().split()):
    if q[0] == num:
        q.popleft()

    else:
        l = q.index(num)
        r = len(q) - l
        if l > r:
            for _ in range(r):
                q.appendleft(q.pop())

        else:
            for _ in range(l):
                q.append(q.popleft())

        q.popleft()
        result += min(l, r)

print(result)
