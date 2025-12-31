# BAEKJOON ONLINE JUDGE - 27501. RGB트리

- [문제출처](https://www.acmicpc.net/problem/27501 '27501. RGB트리')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 트리
- 트리에서의 다이나믹 프로그래밍
- 역추적

## 풀이

### 접근

- `DFS` + `DP`

### 점화식

```python

def dfs(now):
    visited[now] = 1
    for i in range(3):
        dp[now][i] = arr[now - 1][i]

    for node in graph[now]:
        if visited[node]:
            continue

        dfs(node)
        dp[now][0] += max(dp[node][1], dp[node][2])
        dp[now][1] += max(dp[node][0], dp[node][2])
        dp[now][2] += max(dp[node][0], dp[node][1])

```

### 설계

- dp로 RGB 중 하나를 선택하는 경우의 최댓값을 저장
- DFS로 가장 큰 값이 되는 경우의 경로 추적 수행
