# BAEKJOON ONLINE JUDGE - 12784. 인하니카 공화국

- [문제출처](https://www.acmicpc.net/problem/12784 '12784. 인하니카 공화국')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 트리
- 깊이 우선 탐색
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + `DFS`

### 점화식

```python

def dfs(now):
    if dp[now] != INF:
        return dp[now]

    cost = 0
    for node, c in graph[now]:
        if visited[node]:
            dp[now] = min(dp[now], c)
            continue

        visited[node] = 1
        cost += dfs(node)

    if cost:
        dp[now] = min(cost, dp[now])

    return dp[now]

```

### 설계

- 루트에서 현재 노드까지 지나온 경로 중에 최솟값을 저장하는 dp배열 생성
- DFS로 루트노드에서 시작해 리프노드까지 탐색하며 지나온 다이너마이트 개수 중 가장 작은 값을 dp배열에 갱신
- 방문 체크로 중복 탐색을 방지하고 이미 방문한 노드는 현재 노드 위치의 dp배열에 갱신
