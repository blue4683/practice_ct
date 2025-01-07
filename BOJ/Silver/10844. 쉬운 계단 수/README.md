# BAEKJOON ONLINE JUDGE - 10844. 쉬운 계단 수

- [문제출처](https://www.acmicpc.net/problem/10844 '10844. 쉬운 계단 수')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, 10):
    dp[1][i] = 1

for k in range(2, n + 1):
    for i in range(10):
        if not i:
            dp[k][i] = dp[k - 1][i + 1]

        elif i == 9:
            dp[k][i] = dp[k - 1][i - 1]

        else:
            dp[k][i] = dp[k - 1][i - 1] + dp[k - 1][i + 1]

```

### 설계

- `k` 자리수의 가장 큰 자리의 숫자가 `i`인 수의 개수를 테이블에 저장하며 탐색
