from collections import deque


def topological_sort():
    q = deque([x for x in range(1, n + 1) if not indegree[x]])
    visited = []
    while q:
        if len(q) > 1:
            return 'NO'
        
        x = q.popleft()
        visited.append(x)
        for xx in graph[x]:                
            indegree[xx] -= 1
            if not indegree[xx]:
                q.append(xx)

    return 'YES' if len(visited) == n else 'NO'


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(topological_sort())
