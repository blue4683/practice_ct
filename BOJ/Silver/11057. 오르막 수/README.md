# BAEKJOON ONLINE JUDGE - 11057. 오르막 수

- [문제출처](https://www.acmicpc.net/problem/11057 '11057. 오르막 수')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j:])

```

### 설계

- 길이가 `i`인 수 중 `j`로 시작하는 수의 개수를 테이블에 저장하며 탐색
