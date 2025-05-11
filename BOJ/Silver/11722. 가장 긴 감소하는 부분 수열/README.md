# BAEKJOON ONLINE JUDGE - 11722. 가장 긴 감소하는 부분 수열

- [문제출처](https://www.acmicpc.net/problem/11722 '11722. 가장 긴 감소하는 부분 수열')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)


```

### 설계

- 현재 위치 이전의 수와 비교해 현재 수가 작다면 dp테이블 업데이트
