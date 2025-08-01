# BAEKJOON ONLINE JUDGE - 2248. 이진수 찾기

- [문제출처](https://www.acmicpc.net/problem/2248 '2248. 이진수 찾기')

## 알고리즘 분류

- 수학
- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp[0][0] = 1
for j in range(1, n + 1):
    dp[j][0] = 1
    for k in range(1, l + 1):
        dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k]

result = ''
for j in range(n, 0, -1):
    cnt = sum(dp[j - 1][:l + 1])
    if cnt < i:
        result += '1'
        i -= cnt
        l -= 1

    else:
        result += '0'

```

### 설계

- 먼저 `n`자리 이하 이진수 중 `1`을 `l`개 이하로 사용하는 경우를 2차원 dp 배열에 저장
  - 이는 `n - 1`자리 이진수 중 `1` 또는 `0`을 추가하는 경우의 합과 같음 == `dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k]`
- 다음으로 `n`자리부터 각 자리에 맞는 비트를 탐색
  - 현재 자리 `k`에서 `dp[k - 1][0] ~ dp[k - 1][l]`의 모든 경우의 수를 더했을 때 이 값이 `i`보다 큰 경우는 `1`이 붙고 아닌경우는 `0`이 붙는 경우
  - `1`이 붙는 경우 `i`는 위에서 구한 경우의 수의 합을 빼주고, `l`은 `1`을 빼줌
  - 이 과정을 반복해 1의 자리까지 구함
