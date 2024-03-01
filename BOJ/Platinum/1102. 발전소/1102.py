import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
power = input().rstrip()
p = int(input())

bits = 0
on = 0
for i in range(n):
    if power[i] == 'Y':
        bits |= (1 << i)
        on += 1

target = p - on
if target <= 0:
    print(0)

elif on == 0:
    print(-1)

else:
    dp = [[-1] * (1 << n) for _ in range(target + 1)]
    dp[0][bits] = 0

    for bit in range(bits, 1 << n):
        for i in range(1, target + 1):
            if dp[i - 1][bit] != -1:
                for now in range(n):
                    if bit & (1 << now):
                        for next in range(n):
                            if next != now and bit & (1 << next) == 0:
                                next_bit = bit | (1 << next)
                                cost = costs[now][next]
                                if dp[i][next_bit] == -1:
                                    dp[i][next_bit] = dp[i - 1][bit] + cost

                                else:
                                    dp[i][next_bit] = min(
                                        dp[i][next_bit], dp[i - 1][bit] + cost)

    answer = 1e9
    for i in range(1 << n):
        if dp[target][i] != -1:
            answer = min(dp[target][i], answer)

    print(answer)
