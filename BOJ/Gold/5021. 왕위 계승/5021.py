from collections import defaultdict, deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
king = input().rstrip()
royal = defaultdict(float)
royal[king] = 1

graph = defaultdict(list)
indegree = defaultdict(int)
names = set()
for _ in range(n):
    c, a, b = input().split()
    indegree[c] += 2
    graph[a].append(c)
    graph[b].append(c)
    names |= {a, b, c}

q = deque()
for name in names:
    if not indegree[name]:
        q.append(name)

while q:
    x = q.popleft()
    for xx in graph[x]:
        indegree[xx] -= 1
        royal[xx] += royal[x] * 0.5
        if not indegree[xx]:
            q.append(xx)

result, r = '', 0
for _ in range(m):
    name = input().rstrip()
    if royal[name] > r:
        result, r = name, royal[name]

print(result)
