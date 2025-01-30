import sys
input = sys.stdin.readline
INF = 10 ** 9

for _ in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))
    prefix_sum = [0] * (k + 1)
    for i in range(1, k + 1):
        prefix_sum[i] = files[i - 1] + prefix_sum[i - 1]

    dp = [[INF] * k for _ in range(k)]
    for i in range(k):
        dp[i][i] = 0

    for i in range(2, k + 1):
        for j in range(k - i + 1):
            for l in range(j, j + i - 1):
                dp[j][j + i - 1] = min(dp[j][j + i - 1], dp[j][l] + dp[l + 1]
                                       [j + i - 1] + prefix_sum[j + i] - prefix_sum[j])

    print(dp[0][k - 1])
