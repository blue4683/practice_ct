def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    INF = 10 ** 9
    temperature += 10
    t1 += 10
    t2 += 10
    time = len(onboard)
    dp = [[INF] * 52 for _ in range(time + 1)]
    dp[0][temperature] = 0
    for i in range(1, time):
        if onboard[i]:
            max_temp = t2
            min_temp = t1
            
        else:
            max_temp = max(t2, temperature)
            min_temp = min(t1, temperature)
            
        for temp in range(min_temp, max_temp + 1):
            if temperature < t1:
                if temp != temperature:
                    dp[i][temp] = min(dp[i - 1][temp - 1] + a, dp[i - 1][temp] + b, dp[i - 1][temp + 1])
                    
                else:
                    dp[i][temp] = min(dp[i - 1][temp], dp[i - 1][temp - 1] + a, dp[i - 1][temp + 1])
                
            else:
                if temp != temperature:
                    dp[i][temp] = min(dp[i - 1][temp - 1], dp[i - 1][temp] + b, dp[i - 1][temp + 1] + a)

                else:
                    dp[i][temp] = min(dp[i - 1][temp - 1], dp[i - 1][temp])
    
    answer = min(dp[time - 1])
    return answer
