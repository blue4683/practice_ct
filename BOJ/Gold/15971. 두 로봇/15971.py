from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([(s, 0, 0)])
    while q:
        x, dist, mx = q.popleft()
        if x == e:
            return dist - mx

        for xx, c in graph[x]:
            if visited[xx]:
                continue

            visited[xx] = 1
            q.append((xx, dist + c, max(mx, c)))


n, s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(bfs())
