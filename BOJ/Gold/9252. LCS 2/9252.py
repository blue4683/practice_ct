import sys
input = sys.stdin.readline

a, b = input().rstrip(), input().rstrip()
n, m = map(len, [a, b])

dp = [[0] * (m + 1) for _ in range(n + 1)]
for y in range(1, n + 1):
    for x in range(1, m + 1):
        if a[y - 1] == b[x - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1

        else:
            dp[y][x] = max(dp[y][x - 1], dp[y - 1][x])

print(dp[n][m])

result = []
y, x = n, m
while y and x:
    if dp[y - 1][x] == dp[y][x]:
        y -= 1

    elif dp[y][x - 1] == dp[y][x]:
        x -= 1

    else:
        result.append(a[y - 1])
        y -= 1
        x -= 1

print(''.join(result[::-1]))
