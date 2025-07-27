from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
impossible = defaultdict(int)
for a, b, c, d in [map(int, input().split()) for _ in range(k)]:
    impossible[((b, a), (d, c))] = 1
    impossible[((d, c), (b, a))] = 1

dp = [[0] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 1
for y in range(m + 1):
    for x in range(n + 1):
        if (y, x) == (0, 0):
            continue

        if y and not impossible[((y - 1, x), (y, x))]:
            dp[y][x] += dp[y - 1][x]

        if x and not impossible[((y, x - 1), (y, x))]:
            dp[y][x] += dp[y][x - 1]

print(dp[m][n])
