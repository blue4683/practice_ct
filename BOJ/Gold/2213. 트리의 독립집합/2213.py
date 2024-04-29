import sys
input = sys.stdin.readline


def dfs(node):
    for next in graph[node]:
        graph[next].remove(node)
        dfs(next)

        if dp[next][0] >= dp[next][1]:
            dp[node][0] += dp[next][0]
            path[node][0].update(path[next][0])

        else:
            dp[node][0] += dp[next][1]
            path[node][0].update(path[next][1])

        dp[node][1] += dp[next][0]
        path[node][1].update(path[next][0])

    dp[node][1] += weights[node]


n = int(input())
weights = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]
path = [[set(), set([i])] for i in range(n + 1)]
dfs(1)

if dp[1][0] >= dp[1][1]:
    print(dp[1][0])
    print(" ".join(map(str, sorted(list(path[1][0])))))

else:
    print(dp[1][1])
    print(" ".join(map(str, sorted(list(path[1][1])))))
