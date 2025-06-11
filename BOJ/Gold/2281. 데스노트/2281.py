import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solution(y, x):
    if y == n:
        return 0

    if dp[y][x] != -1:
        return dp[y][x]

    result = (m - x + 1) ** 2 + solution(y + 1, arr[y] + 1)
    if x + arr[y] <= m:
        result = min(result, solution(y + 1, x + arr[y] + 1))

    dp[y][x] = result
    return dp[y][x]


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [[-1] * (m + 3) for _ in range(n + 1)]
print(solution(0, 0))
