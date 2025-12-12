from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
names = input().split()
m = int(input())

indegree = {name: 0 for name in names}
graph = {name: [] for name in names}
for _ in range(m):
    x, y = input().split()
    graph[y].append(x)
    indegree[x] += 1

result = []
for name in indegree.keys():
    if indegree[name]:
        continue

    result.append(name)

result.sort()
print(len(result))
print(*result)

q = deque(result)
result = []
while q:
    x = q.popleft()
    sons = []
    for name in graph[x]:
        indegree[name] -= 1
        if not indegree[name]:
            q.append(name)
            sons.append(name)

    result.append((x, sorted(sons)))

result.sort()
for a, b in result:
    print(a, len(b), *b)
