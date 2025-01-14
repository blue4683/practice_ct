# BAEKJOON ONLINE JUDGE - 1788. 피보나치 수의 확장

- [문제출처](https://www.acmicpc.net/problem/1788 '1788. 피보나치 수의 확장')

## 알고리즘 분류

- 수학
- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(2, m + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

```

### 설계

- 피보나치 수 구현
