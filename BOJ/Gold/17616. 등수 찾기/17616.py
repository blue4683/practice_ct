from collections import deque
import sys
input = sys.stdin.readline


def bfs(sx, arr):
    cnt = 0
    visited = [0] * (n + 1)
    q = deque([sx])
    while q:
        x = q.popleft()
        for xx in arr[x]:
            if visited[xx]:
                continue

            visited[xx] = 1
            cnt += 1
            q.append(xx)

    return cnt


n, m, x = map(int, input().split())
up, down = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    down[a].append(b)
    up[b].append(a)

visited = [0] * (n + 1)
u = bfs(x, up) + 1
v = n - bfs(x, down)

print(u, v)
