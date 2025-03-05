from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([1])
    visited = [10 ** 9] * (n + 1)
    used = [0] * m
    visited[1] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if used[i]:
                continue

            used[i] = 1
            for node in paths[i]:
                if visited[node] < visited[now] + 1:
                    continue

                visited[node] = visited[now] + 1
                if node == n:
                    return visited[node]

                q.append(node)

    return visited[n] if visited[n] != 10 ** 9 else -1


n, k, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
paths = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    for node in paths[i]:
        graph[node].append(i)

print(bfs())
