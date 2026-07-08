def solution(N, stages):
    answer = []
    arr = [0] * (N + 2)
    for i in stages:
        arr[i] += 1
        
    dp = [0] * (N + 2)
    dp[N + 1] = arr[N + 1]
    for i in range(N, -1, -1):
        dp[i] = dp[i + 1] + arr[i]
    
    rate = [(arr[i] / dp[i] if dp[i] else 0, i) for i in range(1, N + 1)]
    rate.sort(key=lambda x: (-x[0], x[1]))
    for _, i in rate:
        answer.append(i)
        
    return answer
