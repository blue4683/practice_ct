# BAEKJOON ONLINE JUDGE - 2216. 문자열과 점수

- [문제출처](https://www.acmicpc.net/problem/2216 '2216. 문자열과 점수')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp[n][m] = 0
for i in range(n, -1, -1):
    for j in range(m, -1, -1):
        if i < n and j < m:
            dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + [c, a][x[i] == y[j]])

        if i < n:
            dp[i][j] = max(dp[i][j], dp[i + 1][j] + b)

        if j < m:
            dp[i][j] = max(dp[i][j], dp[i][j + 1] + b)

```

### 설계

- 두 문자를 비교하거나 하나의 문자열에 공백을 추가하는 경우를 dp배열에 저장하면서 탐색
