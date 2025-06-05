from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(node, root, cnt):
    visited[node] = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, root, cnt + 1)

        if next_node == root and cnt >= 2:
            cycle[root] = 1
            return


def bfs():
    q = deque([i for i in range(1, n + 1) if cycle[i]])
    while q:
        x = q.popleft()
        for node in graph[x]:
            if result[node - 1] != -1:
                continue

            result[node - 1] = result[x - 1] + 1
            q.append(node)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cycle = [0] * (n + 1)
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i, i, 0)

result = [-1] * n
for i in range(1, n + 1):
    if cycle[i]:
        result[i - 1] = 0

bfs()
print(*result)
