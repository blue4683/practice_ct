from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(y, x):
    global result
    if dp[y][x]:
        return dp[y][x]

    dp[y][x] = 1

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if 0 <= yy < n and 0 <= xx < n and forest[yy][xx] > forest[y][x]:
            dp[y][x] = max(dp[y][x], dfs(yy, xx) + 1)

    return dp[y][x]


n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
result = 0

for y in range(n):
    for x in range(n):
        result = max(dfs(y, x), result)

print(result)
