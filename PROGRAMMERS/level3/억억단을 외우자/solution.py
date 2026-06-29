def solution(e, starts):
    answer = []
    arr = [1] * (e + 1)
    for i in range(2, e + 1):
        for j in range(1, e // i + 1):
            arr[i * j] += 1
    
    dp = [0] * (e + 1)
    dp[e] = e
    for i in range(e - 1, 0, -1):
        dp[i] = i if arr[i] >= arr[dp[i + 1]] else dp[i + 1]
            
    answer = [dp[s] for s in starts]
    return answer
