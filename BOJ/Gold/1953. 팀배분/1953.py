from collections import deque
import sys
input = sys.stdin.readline


def bfs(i):
    q = deque([i])
    visited[i] = 1
    while q:
        x = q.popleft()
        for xx in dislike[x]:
            if visited[xx]:
                continue

            visited[xx] = -visited[x]
            q.append(xx)


n = int(input())
dislike = [[i] for i in range(n + 1)]
edges = []
for i in range(1, n + 1):
    _, *d = map(int, input().split())
    edges.append(set(d))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if j in edges[i - 1] and i in edges[j - 1]:
            dislike[i].append(j)
            dislike[j].append(i)

visited = [0] * (n + 1)
for i in range(1, n + 1):
    if visited[i]:
        continue

    bfs(i)

a, b = [], []
for i in range(1, n + 1):
    if visited[i] == 1:
        a.append(i)

    else:
        b.append(i)

print(len(a))
print(*a)
print(len(b))
print(*b)
