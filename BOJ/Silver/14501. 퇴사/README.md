# BAEKJOON ONLINE JUDGE - 14501. 퇴사

- [문제출처](https://www.acmicpc.net/problem/14501 '14501. 퇴사')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 브루트포스

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n - 1, -1, -1):
    time, cost = counsels[i]
    if i + time > n:
        dp[i] = dp[i + 1]

    else:
        dp[i] = max(dp[i + 1], dp[i + time] + cost)

```

### 설계

- 상담이 가능한 경우 상담했을 때의 비용을 더한 값과 비교해서 업데이트
- 상담이 불가능한 경우 그 전날 비용으로 업데이트
