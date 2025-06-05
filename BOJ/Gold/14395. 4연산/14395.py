from collections import deque
import sys
input = sys.stdin.readline
ops = ['*', '+', '-', '/']


def operate(num, op):
    if op == '*':
        return num * num

    if op == '+':
        return num + num

    if op == '-':
        return num - num

    if op == '/':
        return num // num


def bfs():
    if s == t:
        return 0

    visited = set()
    q = deque([(s, '')])
    while q:
        num, op = q.popleft()
        if num == t:
            return op

        for o in ops:
            if o == '/' and not num:
                continue

            snum = operate(num, o)
            if snum in visited or snum < 1 or snum > 10 ** 9:
                continue

            visited.add(snum)
            q.append((snum, op + o))

    return -1


s, t = map(int, input().split())
print(bfs())
