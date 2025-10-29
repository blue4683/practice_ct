import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    global result
    visited[now] = 1
    cnt = 0
    for node in graph[now]:
        if arr[node]:
            cnt += 1

        elif not visited[node]:
            cnt += dfs(node)

    return cnt


n = int(input())
arr = [0] + list(map(int, list(input().rstrip())))

result = 0
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    if arr[u] and arr[v]:
        result += 2

visited = [0] * (n + 1)
for s in range(1, n + 1):
    if arr[s] or visited[s]:
        continue

    visited[s] = 1
    cnt = dfs(s)
    result += cnt * (cnt - 1)

print(result)
