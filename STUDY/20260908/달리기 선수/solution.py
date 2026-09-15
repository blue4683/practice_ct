INF = 10 ** 9

d = int(input())
dp = [INF] * (d + 1)
dp[0] = 0
for i in range(1, int(d ** 0.5) + 1):
    dp[i ** 2] = 0
    
for i in range(1, d + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)
        
print(dp[d] + 1)
