import sys
input = sys.stdin.readline


def find(s, e):
    if dp[s][e] != -1:
        return dp[s][e]

    if arr[s] != arr[e]:
        dp[s][e] = 0
        return 0

    if dp[s + 1][e - 1] == -1:
        dp[s + 1][e - 1] = find(s + 1, e - 1)
        dp[s][e] = dp[s + 1][e - 1]

    return dp[s + 1][e - 1]


n = int(input())
arr = list(map(int, input().split()))

dp = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1):
        dp[i][j] = 1

m = int(input())
for s, e in [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]:
    if dp[s][e] == -1:
        print(find(s, e))

    else:
        print(dp[s][e])
