from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [0] * (n + 1)
    visited[a] = 1
    q = deque([a])
    while q:
        x = q.popleft()
        for y in graph[x]:
            if visited[y]:
                continue

            if y == b:
                return visited[x]

            visited[y] = visited[x] + 1
            q.append(y)

    return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs())
