from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([(1, visited[1])])
    while q:
        x, fan = q.popleft()
        if not graph[x] and not fan:
            return 'yes'

        for xx in graph[x]:
            q.append((xx, fan | visited[xx]))

    return 'Yes'


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [0] * (n + 1)
s = int(input())
for x in map(int, input().split()):
    visited[x] = 1

print(bfs())
