# BAEKJOON ONLINE JUDGE - 2240. 자두나무

- [문제출처](https://www.acmicpc.net/problem/2240 '2240. 자두나무')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, t):
    for j in range(w + 1):
        if j:
            if plums[i] == 1:
                dp[i][j][1] = max(dp[i - 1][j - 1][2], dp[i - 1][j][1]) + 1
                dp[i][j][2] = max(dp[i - 1][j - 1][1], dp[i - 1][j][2])

            else:
                dp[i][j][1] = max(dp[i - 1][j - 1][2], dp[i - 1][j][1])
                dp[i][j][2] = max(dp[i - 1][j - 1][1], dp[i - 1][j][2]) + 1

        else:
            if plums[i] == 1:
                dp[i][0][1] = dp[i - 1][0][1] + 1
                dp[i][0][2] = dp[i - 1][0][2]

            else:
                dp[i][0][1] = dp[i - 1][0][1]
                dp[i][0][2] = dp[i - 1][0][2] + 1

```

### 설계

- 자리를 이동한 횟수와 현재 자리에서 받을 수 있는 자두의 수를 저장하며 탐색
