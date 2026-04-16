import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    cards = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = cards[i]

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = max(cards[l] - dp[l + 1][r], cards[r] - dp[l][r - 1])

    score = sum(cards)
    print((score + dp[0][n - 1]) // 2)
