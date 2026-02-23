from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [[-1, -1] for _ in range(n + 1)]
    visited[r] = [0, 0]
    num = 1
    q = deque([(r)])
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if visited[xx][0] != -1:
                continue

            num += 1
            visited[xx] = [visited[x][0] + 1, num]
            q.append(xx)

    return visited


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

visited = bfs()
result = 0
for x in range(1, n + 1):
    if visited[x][0] == -1:
        continue

    result += visited[x][0] * visited[x][1]

print(result)
