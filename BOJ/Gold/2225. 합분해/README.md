# BAEKJOON ONLINE JUDGE - 2225. 합분해

- [문제출처](https://www.acmicpc.net/problem/2225 '2225. 합분해')

## 알고리즘 분류

- 수학
- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(k + 1):
    dp[0][i] = 1

for x in range(1, n + 1):
    for y in range(1, k + 1):
        for z in range(x + 1):
            dp[x][y] += dp[z][y - 1]

        dp[x][y] %= MOD

```

### 설계

- 어떤 수를 탐색할 때 이전 수 한개를 더하는 경우와 더하지 않는 경우를 더해가며 업데이트
