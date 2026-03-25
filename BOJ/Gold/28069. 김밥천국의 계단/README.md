# BAEKJOON ONLINE JUDGE - 28069. 김밥천국의 계단

- [문제출처](https://www.acmicpc.net/problem/28069 '28069. 김밥천국의 계단')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [INF] * (10 ** 6 + 1)
for i in range(1, 4):
    dp[i] = i

for i in range(3, n + 1):
    if i + 1 <= n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    if i + i // 2 <= n:
        dp[i + i // 2] = min(dp[i + i // 2], dp[i] + 1)

```

### 설계

- `0`과 `1`에서 2번째 행동으로 제자리에 있을 수 있어서 `n`에 도착할 때 오르는 횟수가 `k`보다 작아도 가능
- dp 배열에 `x`로 이동할 때 오르는 횟수의 최솟값을 저장하며 탐색
