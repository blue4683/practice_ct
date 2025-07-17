# BAEKJOON ONLINE JUDGE - 2666. 벽장문의 이동

- [문제출처](https://www.acmicpc.net/problem/2666 '2666. 벽장문의 이동')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 브루트포스

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(depth, a, b):
    if depth == m:
        return 0

    v = arr[depth]
    dp[v][a][b] = min(abs(v - a) + dfs(depth + 1, v, b),
                      abs(v - b) + dfs(depth + 1, a, v))
    return dp[v][a][b]


```

### 설계

- 문을 사용했을 때의 최소 거리를 배열에 저장해두고 DFS로 탐색
