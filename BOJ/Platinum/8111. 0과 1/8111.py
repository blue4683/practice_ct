from collections import deque
import sys
input = sys.stdin.readline


def bfs(n):
    q = deque([('1', 1 % n)])
    visited = [0] * (n + 1)
    visited[1 % n] = 1
    while q:
        x, r = q.popleft()
        if not r:
            return x

        for dx in '01':
            xx = x + dx
            rr = (r * 10 + int(dx)) % n
            if len(xx) > 100 or visited[rr]:
                continue

            visited[rr] = 1
            q.append((xx, rr))

    return 'BRAK'


for _ in range(int(input())):
    n = int(input())
    print(bfs(n))
