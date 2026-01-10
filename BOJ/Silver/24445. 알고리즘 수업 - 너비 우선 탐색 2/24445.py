from collections import deque
import sys
input = sys.stdin.readline


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

visited = [0] * (n + 1)
cnt = 1
q = deque([r])
while q:
    x = q.popleft()
    if visited[x]:
        continue

    visited[x] = cnt
    cnt += 1
    for xx in graph[x]:
        if visited[xx]:
            continue

        q.append(xx)

for i in range(1, n + 1):
    print(visited[i])
