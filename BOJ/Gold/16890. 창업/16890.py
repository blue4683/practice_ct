from collections import deque
import sys
input = sys.stdin.readline

a = sorted(list(input().rstrip()))
b = sorted(list(input().rstrip()), reverse=True)
n = len(a)

a = deque(a[:n - n // 2])
b = deque(b[:n // 2])

s, e = '', ''
for turn in range(n):
    if turn % 2:
        if not a or a[0] < b[0]:
            s += b.popleft()

        else:
            e += b.pop()

    else:
        if not b or a[0] < b[0]:
            s += a.popleft()

        else:
            e += a.pop()

print(s + e[::-1])
