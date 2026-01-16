import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
d = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}


def dfs(y, x):
    visited[y][x] = 1
    dy, dx = d[arr[y][x]]
    yy, xx = y + dy, x + dx
    if yy < 0 or yy >= n or xx < 0 or xx >= m:
        dp[y][x] = 1
        return 1

    if dp[yy][xx]:
        dp[y][x] = dp[yy][xx]
        return dp[yy][xx]

    if visited[yy][xx]:
        dp[y][x] = -1
        return -1

    dp[y][x] = dfs(yy, xx)
    return dp[y][x]


n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

dp = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if dp[y][x]:
            continue

        dfs(y, x)

print(sum(map(lambda x: x.count(1), dp)))
