from collections import deque
import sys
input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    cmd = input().split()
    if len(cmd) == 2:
        q.append(int(cmd[1]))

    else:
        if cmd[0] == 'front':
            print(q[0]) if q else print(-1)

        elif cmd[0] == 'back':
            print(q[-1]) if q else print(-1)

        elif cmd[0] == 'pop':
            print(q.popleft()) if q else print(-1)

        elif cmd[0] == 'size':
            print(len(q))

        else:
            print(int(len(q) == 0))
