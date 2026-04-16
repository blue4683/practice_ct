# BAEKJOON ONLINE JUDGE - 11062. 카드 게임

- [문제출처](https://www.acmicpc.net/problem/11062 '11062. 카드 게임')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 게임 이론

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n):
    dp[i][i] = cards[i]

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        dp[l][r] = max(cards[l] - dp[l + 1][r], cards[r] - dp[l][r - 1])

```

### 설계

- 범위 안에서 상대보다 점수를 많이 얻을 수 있는 경우를 dp 배열에 저장하며 탐색
- 최종적으로 0 ~ n - 1 구간에서 상대와의 점수 차를 구해 전체 점수에 더한 뒤 2로 나누면 자신의 점수를 구할 수 있음
