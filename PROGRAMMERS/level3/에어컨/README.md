# Programmers - Level 3. 에어컨

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/214289 "Level 3. 에어컨")

## 알고리즘 분류

- DP

## 풀이

### 접근

- `DP`

### 점화식

```python

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

```

### 설계

- 현재 시간의 탑승 승객에 따라 최소, 최대 온도를 갱신하고 그 범위에서 온도를 유지 또는 상승, 하강 시켰을 때의 최소 비용을 dp배열에 저장