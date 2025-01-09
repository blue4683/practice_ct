# BAEKJOON ONLINE JUDGE - 2156. 포도주 시식

- [문제출처](https://www.acmicpc.net/problem/2156 '2156. 포도주 시식')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, n):
    dp[i][0] = max(dp[i][0], max(dp[i - 1]))
    for j in range(1, 3):
        if j != 1 and not dp[i - 1][j - 1]:
            continue

        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + wines[i])

```

### 설계

- 포도주를 연속으로 마신 개수를 인덱스로 테이블에 저장
