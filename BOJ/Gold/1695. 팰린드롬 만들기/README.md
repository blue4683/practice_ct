# BAEKJOON ONLINE JUDGE - 1695. 팰린드롬 만들기

- [문제출처](https://www.acmicpc.net/problem/1695 '1695. 팰린드롬 만들기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[-i] == arr[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

```

### 설계

- 주어진 수열과 이를 뒤집은 수열을 비교해 LCS 길이를 구한 뒤 `n`에서 빼 최소한의 필요한 개수를 탐색
