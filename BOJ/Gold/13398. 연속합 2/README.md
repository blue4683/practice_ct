# BAEKJOON ONLINE JUDGE - 13398. 연속합 2

- [문제출처](https://www.acmicpc.net/problem/13398 '13398. 연속합 2')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[-10 ** 9] * 2 for _ in range(n)]
dp[0][0] = arr[0]

for i in range(1, n):
    dp[i][0] = max(arr[i], dp[i - 1][0] + arr[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])

```

### 설계

- dp테이블에 현재 위치 이전의 연속합에 현재값을 더한 값과 현재값을 비교해 저장
- 수를 하나 제거하는 경우는 현재 위치 이전의 연속합과 현재 위치 이전의 연속합 중에 하나를 제거한 경우에서 현재 값을 더한 경우와 비교해 저장
