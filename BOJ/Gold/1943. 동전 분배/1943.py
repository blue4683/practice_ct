import sys
input = sys.stdin.readline

try:
    while 1:
        n = int(input())
        coins = []
        half = 0
        for _ in range(n):
            value, cnt = map(int, input().split())
            half += value * cnt
            coins.append((value, cnt))

        if half % 2:
            print(0)

        else:
            half //= 2
            dp = [0] * 100001
            dp[0] = 1
            for i in range(n):
                value, cnt = coins[i]
                for v in range(half + 1, 0, -1):
                    if dp[v - value]:
                        for j in range(cnt):
                            if v + j * value > half:
                                break

                            dp[v + j * value] = 1

            print(dp[half])

except:
    exit()
