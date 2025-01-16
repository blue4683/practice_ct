# BAEKJOON ONLINE JUDGE - 1699. 제곱수의 합

- [문제출처](https://www.acmicpc.net/problem/1699 '1699. 제곱수의 합')

## 알고리즘 분류

- 수학
- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(2, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)

```

### 설계

- 찾는 수보다 작은 제곱수들을 빼면서 최소 개수를 찾아 배열에 저장
