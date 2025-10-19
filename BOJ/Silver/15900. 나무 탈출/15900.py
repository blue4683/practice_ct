from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1
    dist = 0
    while q:
        x = q.popleft()
        leaf = 1
        for xx in graph[x]:
            if visited[xx]:
                continue

            leaf = 0
            visited[xx] = visited[x] + 1
            q.append(xx)

        if leaf:
            dist += visited[x] - 1

    return 'Yes' if dist % 2 else 'No'


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs())
