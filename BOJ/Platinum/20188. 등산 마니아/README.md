# BAEKJOON ONLINE JUDGE - 20188. 등산 마니아

- [문제출처](https://www.acmicpc.net/problem/20188 '20188. 등산 마니아')

## 알고리즘 분류

- 수학
- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 트리
- 깊이 우선 탐색
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DFS` + `DP`

### 점화식

```python
def dfs(node, prev):
    global result
    value = 1
    for next_node in graph[node]:
        if prev == next_node:
            continue

        cnt = dfs(next_node, node)
        k = n - cnt
        result += cnt * k + cnt * (cnt - 1) // 2
        value += cnt

    return value
```

### 설계

- 간선마다 지나가는 경로를 모두 더해줌
  - 간선의 아래쪽 노드의 경우 무조건 간선을 지나게 됨(`cnt * (cnt - 1) / 2`)
  - 간선의 아래쪽 노드가 아닌 노드 끼리 선택할 경우 간선을 지나지 않음(`0`)
  - 간선의 아래쪽 노드와 아닌 노드를 하나씩 선택할 경우 무조건 간선을 지남(`cnt * (n - cnt)`)
- `DFS`를 통해 탐색하면서 각 정점의 자식 노드의 개수 `cnt`를 구해 위의 경우의 수를 구해 모두 결과값에 더해줌
