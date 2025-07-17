import sys
input = sys.stdin.readline


def dfs(depth, a, b):
    if depth == m:
        return 0

    v = arr[depth]
    dp[v][a][b] = min(abs(v - a) + dfs(depth + 1, v, b),
                      abs(v - b) + dfs(depth + 1, a, v))
    return dp[v][a][b]


n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [int(input()) for _ in range(m)]

dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
print(dfs(0, a, b))
