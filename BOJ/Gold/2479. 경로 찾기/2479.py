from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([(a, [a])])
    visited = [0] * (n + 1)
    visited[a] = 1
    while q:
        x, route = q.popleft()
        if x == b:
            return route

        for xx in graph[x]:
            if visited[xx]:
                continue

            visited[xx] = 1
            q.append((xx, route + [xx]))

    return [-1]


n, k = map(int, input().split())
codes = [list(map(int, input().rstrip())) for _ in range(n)]
a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if i == j:
            continue

        cnt = 0
        for x in range(k):
            if cnt > 1:
                break

            if codes[i - 1][x] != codes[j - 1][x]:
                cnt += 1

        if cnt == 1:
            graph[i].append(j)
            graph[j].append(i)

print(*bfs())
