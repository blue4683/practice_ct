from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque([i for i in range(1, n + 1) if not indegree[i]])
result = [0] * n
t = 1
while t:
    new_q = []
    while q:
        x = q.popleft()
        result[x - 1] = t
        for xx in graph[x]:
            indegree[xx] -= 1
            if not indegree[xx]:
                new_q.append(xx)

    if not new_q:
        break

    t += 1
    q = deque(new_q)

print(*result)
