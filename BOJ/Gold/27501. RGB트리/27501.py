import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def trace(now, pcolor):
    visited[now] = 1
    tmp = 0
    index = -1
    for i in range(3):
        if pcolor == i:
            continue

        if dp[now][i] > tmp:
            index = i
            tmp = dp[now][i]

    result[now - 1] = colors[index]
    for node in graph[now]:
        if visited[node]:
            continue

        trace(node, index)


def dfs(now):
    visited[now] = 1
    for i in range(3):
        dp[now][i] = arr[now - 1][i]

    for node in graph[now]:
        if visited[node]:
            continue

        dfs(node)
        dp[now][0] += max(dp[node][1], dp[node][2])
        dp[now][1] += max(dp[node][0], dp[node][2])
        dp[now][2] += max(dp[node][0], dp[node][1])


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

arr = [list(map(int, input().split())) for _ in range(n)]

colors = ['R', 'G', 'B']
dp = [[0] * 3 for _ in range(n + 1)]
visited = [0] * (n + 1)
dfs(1)

print(max(dp[1]))

result = [''] * n
visited = [0] * (n + 1)
trace(1, -1)

print(''.join(result))
