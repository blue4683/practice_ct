# BAEKJOON ONLINE JUDGE - 12869. 뮤탈리스크

- [문제출처](https://www.acmicpc.net/problem/12869 '12869. 뮤탈리스크')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(a, b, c):
    if a < 0:
        return dfs(0, b, c)

    if b < 0:
        return dfs(a, 0, c)

    if c < 0:
        return dfs(a, b, 0)

    if (a, b, c) == (0, 0, 0):
        return 0

    if dp[a][b][c]:
        return dp[a][b][c]

    result = 10 ** 9
    for aa, bb, cc in combs:
        result = min(result, dfs(a - aa, b - bb, c - cc) + 1)

    dp[a][b][c] = result
    return dp[a][b][c]

```

### 설계

- scv의 남은 체력을 인덱스로하는 3차원 배열을 생성하고 공격하는 경우의 수를 dfs로 탐색하면서 모두가 0이 되는 최솟값 출력
