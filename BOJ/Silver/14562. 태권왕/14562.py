from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([(0, s, t)])
    visited = {(s, t)}
    while q:
        cnt, x, y = q.popleft()
        if x == y:
            return cnt

        if x > y:
            continue

        if (x * 2, y + 3) not in visited:
            visited.add((x * 2, y + 3))
            q.append((cnt + 1, x * 2, y + 3))

        if (x + 1, y) not in visited:
            visited.add((x + 1, y))
            q.append((cnt + 1, x + 1, y))

    return 0


for _ in range(int(input())):
    s, t = map(int, input().split())
    print(bfs())
