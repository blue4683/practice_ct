# BAEKJOON ONLINE JUDGE - 2193. 이친수

- [문제출처](https://www.acmicpc.net/problem/2193 '2193. 이친수')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(2, n + 1):
    dp[i][1] = dp[i - 1][0]
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

```

### 설계

- 앞에 수가 `0`인 경우 `0, 1` 둘 다 올 수 있고, 앞에 수가 `1`인 경우 `0`만 가능
