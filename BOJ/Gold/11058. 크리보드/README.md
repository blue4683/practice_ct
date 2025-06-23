# BAEKJOON ONLINE JUDGE - 11058. 크리보드

- [문제출처](https://www.acmicpc.net/problem/11058 '11058. 크리보드')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(3, i):
        dp[i] = max(dp[i], dp[i - j] * (j - 1))
```

### 설계

- 하나를 출력하는 경우와 (선택, 복사, 붙여넣기)를 하는 경우를 비교해 최댓값을 저장
  - (선택, 복사, 붙여넣기)의 경우 붙여넣기가 가능한 3번 누른 후부터 탐색
