import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(now):
    global d, g
    m = len(graph[now])
    if m >= 3:
        g += m * (m - 1) * (m - 2) // 6

    for node in graph[now]:
        if visited[node]:
            continue

        visited[node] = 1
        dfs(node)
        k = len(graph[node])
        if m >= 2 and k >= 2:
            d += (m - 1) * (k - 1)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

d, g = 0, 0
visited = [0] * (n + 1)
visited[1] = 1
dfs(1)

if d == g * 3:
    print('DUDUDUNGA')

elif d > g * 3:
    print('D')

else:
    print('G')
