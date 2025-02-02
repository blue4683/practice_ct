# BAEKJOON ONLINE JUDGE - 17404. RGB거리 2

- [문제출처](https://www.acmicpc.net/problem/17404 '17404. RGB거리 2')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[INF] * 3 for _ in range(n)]
for color in range(3):
    for i in range(3):
        if color == i:
            dp[0][i] = graph[0][i]

        else:
            dp[0][i] = INF

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][2]

    for i in range(3):
        if i == color:
            continue

        result = min(result, dp[n - 1][i])

```

### 설계

- 맨 처음 칠하는 색을 정하고, 이후부터는 그 전에 칠한 색을 제외한 것들 중 최소 비용을 테이블에 저장하며 탐색
