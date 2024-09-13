from collections import deque
import sys
input = sys.stdin.readline


def bfs(k, v):
    q = deque(videos[v])
    visited = [0] * (n + 1)
    visited[v] = 1
    result = 0

    while q:
        node, usado = q.popleft()
        if visited[node]:
            continue

        visited[node] = 1
        if usado < k:
            continue

        result += 1
        for next_node, next_usado in videos[node]:
            next_usado = min(usado, next_usado)
            q.append((next_node, next_usado))

    return result


n, Q = map(int, input().split())
videos = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, q, r = map(int, input().split())
    videos[p].append((q, r))
    videos[q].append((p, r))

for _ in range(Q):
    print(bfs(*map(int, input().split())))
