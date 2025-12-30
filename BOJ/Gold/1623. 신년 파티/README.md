# BAEKJOON ONLINE JUDGE - 1623. 신년 파티

- [문제출처](https://www.acmicpc.net/problem/1623 '1623. 신년 파티')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 트리
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DFS` + `DP`

### 점화식

```python

def dfs(now):
    dp[1][now] = arr[now]
    for node in graph[now]:
        dfs(node)
        dp[0][now] += max(dp[0][node], dp[1][node])
        dp[1][now] += dp[0][node]

```

### 설계

- dp로 참석을 한 경우와 아닌 경우의 최댓값을 저장하며 DFS 수행
- 이후 1번이 참석한 경우와 아닌 경우로 나눠 `n`번이 참석한 경우가 아닌 경우보다 높을 경우 참석으로 생각하여 참가자 번호를 DFS로 추적함
