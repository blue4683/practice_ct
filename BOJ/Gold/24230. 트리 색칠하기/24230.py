import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now, color):
    global result
    if arr[now] != c[now] and color != c[now]:
        result += 1
        color = c[now]

    arr[now] = color
    for node in graph[now]:
        if visited[node]:
            continue

        visited[node] = 1
        dfs(node, color)


n = int(input())
c = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


arr = [0] * (n + 1)
visited = [0] * (n + 1)
visited[1] = 1
result = 0
dfs(1, 0)
print(result)
