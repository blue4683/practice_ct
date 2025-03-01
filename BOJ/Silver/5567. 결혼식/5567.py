import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
for i in graph[1]:
    visited[i] = 1
    if graph[i]:
        for j in graph[i]:
            visited[j] = 1

print(sum(visited) - visited[1])
