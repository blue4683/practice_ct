import sys
input = sys.stdin.readline


def dfs(now):
    visited[now] = 1
    for node in graph[now]:
        if visited[node]:
            continue

        dfs(node)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

result = [0] * (n + 1)
for node in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(node)
    result = list(map(lambda x, y: x + y, result, visited))

answer = -1
for i in range(1, n + 1):
    if result[i] == n:
        answer = i
        break

print(answer)
