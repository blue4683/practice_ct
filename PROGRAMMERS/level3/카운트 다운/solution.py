def solution(target):
    answer = []
    
    def compare(a, b):
        if a[0] < b[0]:
            return a
        
        elif a[0] == b[0] and a[1] >= b[1]:
            return a
        
        return b
    
    dp = [[10 ** 9, 0] for _ in range(target + 1)]
    dp[0] = [0, 0]
    for i in range(1, min(target + 1, 21)):
        dp[i] = [1, 1]
        
    for i in range(21, target + 1):
        for j in range(1, 21):
            dp[i] = compare(dp[i], [dp[i - j][0] + 1, dp[i - j][1] + 1])
            if i - j * 2 >= 0:
                dp[i] = compare(dp[i], [dp[i - j * 2][0] + 1, dp[i - j * 2][1]])
                
            if i - j * 3 >= 0:
                dp[i] = compare(dp[i], [dp[i - j * 3][0] + 1, dp[i - j * 3][1]])
        
        if i - 50 >= 0:
            dp[i] = compare(dp[i], [dp[i - 50][0] + 1, dp[i - 50][1] + 1])
            
    answer = dp[target]
    return answer
