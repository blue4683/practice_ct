from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i] = list(map(int, input().split()))[:-1]

m = int(input())
q = deque(list(map(int, input().split())))
visited = [0] * (n + 1)
rumor = [0] * (n + 1)
for i in q:
    visited[i] = 1

while q:
    x = q.popleft()
    for xx in graph[x]:
        if visited[xx]:
            continue

        rumor[xx] += 1
        if rumor[xx] >= len(graph[xx]) // 2 + len(graph[xx]) % 2:
            visited[xx] = visited[x] + 1
            q.append(xx)

print(*map(lambda x: x - 1, visited[1:]))
