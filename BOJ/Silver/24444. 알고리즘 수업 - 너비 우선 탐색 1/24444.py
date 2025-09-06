from collections import deque
import sys
input = sys.stdin.readline


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

order = 1
visited = [0] * (n + 1)
visited[r] = order
q = deque([r])
while q:
    x = q.popleft()
    for y in graph[x]:
        if visited[y]:
            continue

        visited[y] = order + 1
        order += 1
        q.append(y)

for i in range(1, n + 1):
    print(visited[i])
