from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    k, *arr = list(map(int, input().split()))
    for i in range(k - 1):
        graph[arr[i]].append(arr[i + 1])
        indegree[arr[i + 1]] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i]:
        continue

    q.append(i)

result = []
while q:
    x = q.popleft()
    result.append(x)
    for node in graph[x]:
        indegree[node] -= 1
        if not indegree[node]:
            q.append(node)

if len(result) == n:
    for res in result:
        print(res)

else:
    print(0)
