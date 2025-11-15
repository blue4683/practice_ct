# BAEKJOON ONLINE JUDGE - 12978. 스크루지 민호 2

- [문제출처](https://www.acmicpc.net/problem/12978 '12978. 스크루지 민호 2')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 트리
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + `DFS`

### 점화식

```python

def dfs(now):
    for node in graph[now]:
        if visited[node]:
            continue

        visited[node] = 1
        no, yes = dfs(node)
        dp[now][0] += yes
        dp[now][1] += min(yes, no)

    return dp[now]

dp = [[0, 1] for _ in range(n + 1)]

```

### 설계

- 현재 노드에 경찰서를 설치하는 경우와 아닌 경우를 테이블에 갱신하며 DFS 탐색
  - 경찰서를 설치하는 경우는 다음 노드에서 설치 여부 고려 X
  - 경찰서를 설치하지 않는 경우는 다음 노드에서 무조건 설치
