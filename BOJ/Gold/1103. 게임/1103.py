import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
INF = 10 ** 9
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m or arr[y][x] == 'H':
        return 1

    return 0


def dfs(y, x):
    if out_of_range(y, x):
        return 0

    if visited[y][x]:
        print(-1)
        exit()

    if dp[y][x] != -1:
        return dp[y][x]

    visited[y][x] = 1
    result = -INF
    k = int(arr[y][x])
    for dy, dx in d:
        yy, xx = y + k * dy, x + k * dx
        result = max(result, dfs(yy, xx) + 1)

    dp[y][x] = result
    visited[y][x] = 0
    return dp[y][x]


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(dfs(0, 0))
