from collections import deque
import sys
input = sys.stdin.readline


def bfs(s):
    q = deque([s])
    visited[s] = 1
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if visited[xx] and visited[x] == visited[xx]:
                return 0

            if not visited[xx]:
                visited[xx] = -visited[x]
                q.append(xx)

    return 1


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        if not bfs(i):
            print(0)
            exit()

print(1)
