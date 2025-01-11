# BAEKJOON ONLINE JUDGE - 9465. 스티커

- [문제출처](https://www.acmicpc.net/problem/9465 '9465. 스티커')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for x in range(1, n):
    dp[0][x] = max(dp[0][x], dp[0][x - 1], dp[1][x - 1],
                    dp[1][x - 1] + stickers[0][x])
    dp[1][x] = max(dp[1][x], dp[0][x - 1], dp[1][x - 1],
                    dp[0][x - 1] + stickers[1][x])

```

### 설계

- `x`가 커지는 방향으로 탐색 진행
- 스티커를 선택하지 않고 이전 열의 같은 행 또는 다른 행의 값을 사용하거나, 스티커를 선택하고 이전 열의 다른 행의 값에서 스티커 점수를 더한 값 중 최댓값을 저장
