import sys

input = sys.stdin.readline
INF = int(1e9)


def dfs(now, visited):
    if visited == (1 << n) - 1:
        if cost[now][0]:
            return cost[now][0]
        else:
            return INF

    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = INF
    for next in range(1, n):
        if not cost[now][next] or visited & (1 << next):
            continue

        min_cost = min(min_cost, dfs(next, visited | (1 << next)) + cost[now][next])

    dp[(now, visited)] = min_cost
    return dp[(now, visited)]


n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]
dp = dict()

print(dfs(0, 1))
