# BAEKJOON ONLINE JUDGE - 1983. 숫자 박스

- [문제출처](https://www.acmicpc.net/problem/1983 '1983. 숫자 박스')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(cur, i, j):
    if (i, j) == (m, k):
        return 0

    if cur == n:
        return INF

    if dp[cur][i][j] != INF:
        return dp[cur][i][j]

    result = dp[cur][i][j]
    if i < m and j < k:
        result = max(result, arr1[i] * arr2[j] + dfs(cur + 1, i + 1, j + 1))

    if i < m:
        result = max(result, dfs(cur + 1, i + 1, j))

    if j < k:
        result = max(result, dfs(cur + 1, i, j + 1))

    dp[cur][i][j] = result
    return dp[cur][i][j]

```

### 설계

- `0`이 아닌 수들을 각각 배열에 저장하고 탐색 수행
- `0`을 사용하는 경우와 아닌 경우를 탐색하여 최댓값을 dp 배열에 업데이트
- 모든 수를 사용하기 전에 전체 길이에 도달한 경우 존재하는 `0`보다 많은 개수를 사용한 것임으로 최솟값 반환
