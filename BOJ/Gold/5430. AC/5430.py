from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    arr = deque(list(input().rstrip().strip('[]').split(',')))
    if not n:
        arr = deque()

    stack = 0
    for rd in p:
        if rd == 'R':
            stack += 1
        else:
            if len(arr):
                if stack % 2:
                    arr.pop()

                else:
                    arr.popleft()

            else:
                print('error')
                break

    else:
        if stack % 2:
            arr.reverse()
            print(f"[{','.join(arr)}]")

        else:
            print(f"[{','.join(arr)}]")
