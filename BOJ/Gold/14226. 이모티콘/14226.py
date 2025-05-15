from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [0] * (2 * s + 1)
    q = deque([(1, 0, 0)])
    while q:
        x, clip, cnt = q.popleft()
        if x == s:
            return cnt

        if not visited[x]:
            visited[x] = 1
            q.append((x, x, cnt + 1))

        if clip and x + clip < 2 * s + 1:
            q.append((x + clip, clip, cnt + 1))

        if x > 0:
            q.append((x - 1, clip, cnt + 1))


s = int(input())
print(bfs())
