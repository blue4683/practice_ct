# BAEKJOON ONLINE JUDGE - 2302. 극장 좌석

- [문제출처](https://www.acmicpc.net/problem/2302 '2302. 극장 좌석')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

```

### 설계

- 연속된 자석을 조건에 맞게 앉을 수 있는 경우의 수를 테이블에 저장
- vip 좌석이 존재할 때 테이블을 사용해 경우의 수 탐색
