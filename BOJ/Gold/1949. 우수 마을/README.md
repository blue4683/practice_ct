# BAEKJOON ONLINE JUDGE - 1949. 우수 마을

- [문제출처](https://www.acmicpc.net/problem/1949 '1949. 우수 마을')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 트리
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(now):
    visited[now] = 1
    dp[now][0] = 0
    dp[now][1] = population[now]

    for next in graph[now]:
        if visited[next]:
            continue

        dfs(next)
        dp[now][0] += max(dp[next][0], dp[next][1])
        dp[now][1] += dp[next][0]

```

### 설계

- 현재 노드가 우수 마을이라면, 다음 노드는 우수 마을이 아님
- 현재 노드가 우수 마을이 아니라면, 다음 노드는 우수 마을일수도 아닐수도 있음
