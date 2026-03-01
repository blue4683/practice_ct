import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    visited[now] = 1
    node = graph[now]
    if not visited[node]:
        dfs(node)


n = int(input())
graph = [0]
for i in range(n):
    graph.append(int(input()))

result, cnt = 0, 0
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i)
    tmp = sum(visited)
    if tmp > cnt:
        result, cnt = i, tmp

print(result)
