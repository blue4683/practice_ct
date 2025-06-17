from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    time, k, *tasks = map(int, input().split())
    cost[i] = time
    indegree[i] = k
    for task in tasks:
        graph[task].append(i)

result = [0] * (n + 1)
q = deque()
for i in range(1, n + 1):
    if indegree[i]:
        continue

    result[i] = cost[i]
    q.append(i)

while q:
    now = q.popleft()
    for node in graph[now]:
        indegree[node] -= 1
        result[node] = max(result[node], result[now] + cost[node])
        if not indegree[node]:
            q.append(node)

print(max(result))
