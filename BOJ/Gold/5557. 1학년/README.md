# BAEKJOON ONLINE JUDGE - 5557. 1학년

- [문제출처](https://www.acmicpc.net/problem/5557 '5557. 1학년')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[0] * 21 for _ in range(n)]
dp[0][arr[0]] = 1

for j in range(1, n - 1):
    for i in range(21):
        if not dp[j - 1][i]:
            continue

        if i + arr[j] <= 20:
            dp[j][i + arr[j]] += dp[j - 1][i]

        if i - arr[j] >= 0:
            dp[j][i - arr[j]] += dp[j - 1][i]

```

### 설계

- 더하거나 빼는 수의 인덱스와 그 수의 전까지의 계산 값을 인덱스로하는 이차원배열 생성
- 0이상 20이하가 되도록 탐색을 진행하고 `n - 2`까지 계산한 값이 `n - 1` 인덱스 위치의 값과 같은 경우의 수를 출력
