# BAEKJOON ONLINE JUDGE - 9177. 단어 섞기

- [문제출처](https://www.acmicpc.net/problem/9177 '9177. 단어 섞기')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색

## 풀이

### 접근

- `DP` + `DFS`

### 점화식

```python

def dfs(y, x):
    if y == n and x == m:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    if y < n and a[y] == c[y + x] and dfs(y + 1, x):
        dp[y][x] = 1
        return dp[y][x]

    if x < m and b[x] == c[y + x] and dfs(y, x + 1):
        dp[y][x] = 1
        return dp[y][x]

    dp[y][x] = 0
    return dp[y][x]

```

### 설계

- DFS를 통해 탐색하고 dp테이블을 업데이트
  - 섞어 만든 단어를 처음부터 탐색할 때, 알파벳은 무조건 둘 중 하나의 단어에 포함되어야 함 == 한쪽에서 사용하지 않았다면 다른쪽에서 사용해야만 함
