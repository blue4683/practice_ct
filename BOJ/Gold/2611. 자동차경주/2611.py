from collections import deque
import sys
input = sys.stdin.readline


n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
last = []
for _ in range(m):
    p, q, r = map(int, input().split())
    if q == 1:
        last.append((p, r))
        continue

    indegree[q] += 1
    graph[p].append((q, r))

parent = [0 for _ in range(n + 1)]
dists = [0] * (n + 1)
q = deque([1])
while q:
    x = q.popleft()
    for xx, cost in graph[x]:
        if dists[xx] < dists[x] + cost:
            dists[xx] = dists[x] + cost
            parent[xx] = x

        indegree[xx] -= 1
        if not indegree[xx]:
            q.append(xx)

result, turn = 0, 0
for x, cost in last:
    if dists[x] + cost > result:
        result, turn = dists[x] + cost, x

path = []
while turn != 1:
    path.append(turn)
    turn = parent[turn]

path.append(1)
path.reverse()
path.append(1)

print(result)
print(*path)
