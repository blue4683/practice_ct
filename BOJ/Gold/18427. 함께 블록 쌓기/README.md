# BAEKJOON ONLINE JUDGE - 18427. 함께 블록 쌓기

- [문제출처](https://www.acmicpc.net/problem/18427 '18427. 함께 블록 쌓기')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 배낭 문제

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[0] * (h + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    dp[i] = dp[i - 1][:]
    for block in students[i - 1]:
        for j in range(block, h + 1):
            dp[i][j] += dp[i - 1][j - block]

```

### 설계

- 2차원 배열을 생성하여 각 사람마다 만들수 있는 높이를 저장
  - `0`을 만들 수 있는 경우는 항상 `1`이므로 `1`로 초기화
