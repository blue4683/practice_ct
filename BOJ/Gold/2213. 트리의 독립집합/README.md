# BAEKJOON ONLINE JUDGE - 2213. 트리의 독립집합

- [문제출처](https://www.acmicpc.net/problem/2213 '2213. 트리의 독립집합')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 트리
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DFS` + `DP`

### 점화식

```python

def dfs(node):
    for next in graph[node]:
        graph[next].remove(node)
        dfs(next)

        if dp[next][0] >= dp[next][1]:
            dp[node][0] += dp[next][0]
            path[node][0].update(path[next][0])

        else:
            dp[node][0] += dp[next][1]
            path[node][0].update(path[next][1])

        dp[node][1] += dp[next][0]
        path[node][1].update(path[next][0])

    dp[node][1] += weights[node]

```

### 설계

- `dp[n][2]` 테이블을 만들어 `dp[node][0]`는 `node`가 속하지 않고, `dp[node][1]`은 `node`가 속하는 집합의 가중치를 저장
- `DFS`를 통해 그래프를 탐색하면서 이동하려는 `next` 노드에서 `node` 간선을 제거하여 돌아가는 것을 방지
- `dp[node][0]`는 `next`가 포함될 경우와 포함되지 않을 경우를 비교해서 큰 값을 더하고, `dp[node][1]`은 포함되지 않는 경우만 더함
- 탐색하면서 가져온 `dp` 위치의 `path`를 업데이트
