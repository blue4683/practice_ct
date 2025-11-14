from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    visited = [0] * (n + 1)
    result = []
    for i in range(1, s + 1):
        visited[i] = 1
        q.append((i, 0))

    while q:
        x, cnt = q.popleft()
        if x == p:
            result.append(cnt)
            continue

        for xx in graph[x]:
            if xx != p and visited[xx]:
                continue

            visited[xx] = 1
            q.append((xx, cnt + 1))

    return result


n, s, p = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = n - 1
cases = bfs()
cases.sort()
for i in range(2):
    result -= cases[i]

print(result)
