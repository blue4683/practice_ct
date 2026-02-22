from collections import deque
import sys
input = sys.stdin.readline


def bfs(sx):
    q = deque([sx])
    visited = [0] * (n + 1)
    visited[sx] = 1
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if visited[xx]:
                continue

            visited[xx] = 1
            q.append(xx)

    return sum(visited) - 1


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

print(bfs(int(input())))
