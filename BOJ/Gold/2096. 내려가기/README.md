# BAEKJOON ONLINE JUDGE - 2096. 내려가기

- [문제출처](https://www.acmicpc.net/problem/2096 '2096. 내려가기')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 슬라이딩 윈도우

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(3):
    dp[0][i] = arr[0][i]

result = []
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][:2]) + arr[i][0]
    dp[i][1] = max(dp[i - 1]) + arr[i][1]
    dp[i][2] = max(dp[i - 1][1:]) + arr[i][2]

result.append(max(dp[-1]))
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][:2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][1:]) + arr[i][2]

```

### 설계

- 내려가면서 가능한 수의 합 중 최댓값과 최솟값을 배열에 저장하며 이후 탐색에 사용
