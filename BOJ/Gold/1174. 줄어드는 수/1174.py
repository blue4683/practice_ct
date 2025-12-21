from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    cnt = 9
    q = deque([i for i in range(1, 10)])
    while q:
        x = q.popleft()
        for i in range(10):
            if i >= (x % 10):
                break

            cnt += 1
            if cnt == n - 1:
                return x * 10 + i

            q.append(x * 10 + i)

    return -1


n = int(input())
if n <= 10:
    print(n - 1)

else:
    print(bfs())
