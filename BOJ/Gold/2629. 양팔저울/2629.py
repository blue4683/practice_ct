import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

dp = [0] * 40001
dp[0] = 1

for w in weights:
    tmp = dp[:]
    for i in range(40001):
        if dp[i]:
            if i + w <= 40000:
                tmp[i + w] = 1

            tmp[abs(i - w)] = 1

    dp = tmp

print(*map(lambda x: 'Y' if dp[x] else 'N', marbles))
