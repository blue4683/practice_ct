# BAEKJOON ONLINE JUDGE - 2294. 동전 2

- [문제출처](https://www.acmicpc.net/problem/2294 '2294. 동전 2')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, k + 1):
    for coin in coins:
        if i - coin < 0:
            continue

        dp[i] = min(dp[i], dp[i - coin] + 1)

```

### 설계

- `1`부터 최소의 경우의 수를 구해 `dp` 테이블에 저장
