MOD = 1000000007
n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
for i in range(n + 1):
    if i + 1 < n + 1:
        dp[i + 1] += dp[i]
        dp[i + 1] %= MOD
        
    if i + 2 < n + 1:
        dp[i + 2] += dp[i]
        dp[i + 2] %= MOD
    
print(dp[n])
