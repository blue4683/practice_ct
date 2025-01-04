# BAEKJOON ONLINE JUDGE - 11055. 가장 큰 증가하는 부분 수열

- [문제출처](https://www.acmicpc.net/problem/11055 '11055. 가장 큰 증가하는 부분 수열')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])


```

### 설계

- 앞에 수보다 큰 경우 더한 값 중에 더 큰 값을 테이블에 저장
