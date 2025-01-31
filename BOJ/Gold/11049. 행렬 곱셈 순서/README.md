# BAEKJOON ONLINE JUDGE - 11049. 행렬 곱셈 순서

- [문제출처](https://www.acmicpc.net/problem/11049 '11049. 행렬 곱셈 순서')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[INF] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for i in range(2, n + 1):
    for j in range(n - i + 1):
        for k in range(j, j + i - 1):
            dp[j][j + i - 1] = min(dp[j][j + i - 1], dp[j][k] + dp[k + 1]
                                   [j + i - 1] + matrixes[j][0] * matrixes[k][1] * matrixes[j + i - 1][1])

```

### 설계

- BOJ - 11066. 파일 합치기 문제와 동일
