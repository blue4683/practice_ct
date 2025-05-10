# BAEKJOON ONLINE JUDGE - 1309. 동물원

- [문제출처](https://www.acmicpc.net/problem/1309 '1309. 동물원')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 3
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901


```

### 설계

- 사자를 `n`행에 놓은 경우와 놓지 않은 경우로 나누어 생각하고 점화식 생성
