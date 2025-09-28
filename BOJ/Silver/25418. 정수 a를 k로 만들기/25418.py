from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([a])
    visited = [0] * (k + 1)
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]

        if x + 1 <= k and not visited[x + 1]:
            visited[x + 1] = visited[x] + 1
            q.append(x + 1)

        if x * 2 <= k and not visited[x * 2]:
            visited[x * 2] = visited[x] + 1
            q.append(x * 2)


a, k = map(int, input().split())
print(bfs())
