from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([s])
    visited = [10 ** 9] * (n + 1)
    visited[s] = 0
    while q:
        x = q.popleft()
        if x == e:
            return visited[x]

        for xx in {x - 1, x + 1, *portal[x]}:
            if xx < 1 or xx > n or visited[xx] <= visited[x] + 1:
                continue

            visited[xx] = visited[x] + 1
            q.append(xx)


n, m = map(int, input().split())
s, e = map(int, input().split())
portal = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    portal[x].append(y)
    portal[y].append(x)

print(bfs())
