def solution(n):
    MOD = 1000000007
    dp = [1] * (n + 4)
    dp[2] = 3
    dp[3] = 10
    
    prefix = [1] * (n + 4)
    for i in range(1, 4):
        prefix[i] = prefix[i - 1] + dp[i]
    
    triple = [0] * (n + 4)
    for i in range(4):
        triple[i] = dp[i]
        if i >= 3:
            triple[i] += triple[i - 3]
            
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + prefix[i - 4] * 2 + triple[i - 6] * 2) % MOD
        prefix[i] = (prefix[i - 1] + dp[i]) % MOD
        triple[i] = (triple[i - 3] + dp[i]) % MOD

    return dp[n]
