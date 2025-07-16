# BAEKJOON ONLINE JUDGE - 2228. 구간 나누기

- [문제출처](https://www.acmicpc.net/problem/2228 '2228. 구간 나누기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(k, depth):
    if k == m:
        return 0

    if depth >= n:
        return -10 ** 9

    if dp[k][depth] != -1:
        return dp[k][depth]

    dp[k][depth] = dfs(k, depth + 1)
    tmp = 0
    for i in range(depth, n):
        tmp += arr[i]
        ret = dfs(k + 1, i + 2) + tmp
        if ret > dp[k][depth]:
            dp[k][depth] = ret

    return dp[k][depth]

```

### 설계

- 구간의 개수와 배열 인덱스를 기준으로 재귀 탐색하여 구간의 최댓값을 구함
