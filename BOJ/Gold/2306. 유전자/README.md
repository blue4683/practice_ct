# BAEKJOON ONLINE JUDGE - 2306. 유전자

- [문제출처](https://www.acmicpc.net/problem/2306 '2306. 유전자')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n - 1):
    if is_koi(i, i + 1):
        dp[i][i + 1] = 2

for i in range(n - 2):
    if dp[i][i + 1] or dp[i + 1][i + 2] or is_koi(i, i + 2):
        dp[i][i + 2] = 2

for k in range(3, n):
    for i in range(n - k):
        dp[i][i + k] = dp[i + 1][i + k - 1] + 2 * is_koi(i, i + k)
        for j in range(k):
            tmp = dp[i][i + j] + dp[i + j + 1][i + k]
            if tmp > dp[i][i + k]:
                dp[i][i + k] = tmp

```

### 설계

- 해당 구간에 존재하는 KOI 유전자의 최대 길이를 dp 배열에 저장하며 탐색
