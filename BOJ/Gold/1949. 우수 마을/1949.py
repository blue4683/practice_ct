import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    visited[now] = 1
    dp[now][0] = 0
    dp[now][1] = population[now]

    for next in graph[now]:
        if visited[next]:
            continue

        dfs(next)
        dp[now][0] += max(dp[next][0], dp[next][1])
        dp[now][1] += dp[next][0]


n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0] * 2 for _ in range(n + 1)]
visited = [0] * (n + 1)

dfs(1)
print(max(dp[1]))
