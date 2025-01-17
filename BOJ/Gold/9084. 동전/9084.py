import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for value in range(1, m + 1):
            if value - coin < 0:
                continue

            dp[value] += dp[value - coin]

    print(dp[m])
