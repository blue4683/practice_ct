import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def trace(now, parent_attend):
    attend = 0
    if not parent_attend:
        if now == 1:
            visited[now] = 1
            attend = 1

        elif dp[1][now] > dp[0][now]:
            visited[now] = 1
            attend = 1

    for node in graph[now]:
        trace(node, attend)


def dfs(now):
    dp[1][now] = arr[now]
    for node in graph[now]:
        dfs(node)
        dp[0][now] += max(dp[0][node], dp[1][node])
        dp[1][now] += dp[0][node]


n = int(input())
arr = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i, p in enumerate(map(int, input().split()), start=2):
    graph[p].append(i)

dp = [[0] * (n + 1) for _ in range(2)]
dfs(1)

print(dp[1][1], dp[0][1])
for i in range(1, -1, -1):
    visited = [0] * (n + 1)
    trace(1, i ^ 1)

    result = [i for i in range(1, n + 1) if visited[i]]
    print(*result, -1)
