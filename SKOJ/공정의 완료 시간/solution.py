from collections import deque


n, m = map(int, input().split())
ts = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

q = deque()
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
        dp[i] = ts[i - 1]
    
while q:
    x = q.popleft()
    for xx in graph[x]:
        indegree[xx] -= 1
        dp[xx] = max(dp[xx], dp[x] + ts[xx - 1])
        if not indegree[xx]:
            q.append(xx)
    
print(max(dp))
