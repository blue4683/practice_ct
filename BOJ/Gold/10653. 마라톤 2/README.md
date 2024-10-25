# BAEKJOON ONLINE JUDGE - 10653. 마라톤 2

- [문제출처](https://www.acmicpc.net/problem/10653 '10653. 마라톤 2')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[INF] * (k + 1) for _ in range(n)]
dp[0][0] = 0

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + distances[i - 1][i]

for i in range(1, k + 1):
    dp[0][i], dp[1][i] = 0, dp[i - 1][1]
    dp[i][i] = distances[i][0]
    for j in range(1, n):
        for l in range(i, 0, -1):
            if j - l - 1 < 0:
                continue

            dp[j][i] = min(dp[j][i], dp[j - l - 1][i - l] +
                           distances[j - l - 1][j], dp[j - 1][i] + distances[j][j - 1])

```

### 설계

- 체크포인트 간 거리를 구한뒤 dp 테이블 생성
- 스킵하지 않았을 때의 거리로 초기화
- 이후 스킵하는 경우와 그렇지 않는 경우를 비교해 dp 테이블 업데이트
