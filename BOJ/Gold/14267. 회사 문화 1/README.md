# BAEKJOON ONLINE JUDGE - 14267. 회사 문화 1

- [문제출처](https://www.acmicpc.net/problem/14267 '14267. 회사 문화 1')

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

def dfs(now, before):
    result[now] = appreciate[now] + result[before]
    for next in graph[now]:
        dfs(next, now)

```

### 설계

- 현재 노드의 칭찬 받은 정도는 `직접 칭찬을 받은 정도 + 이전 노드에서 칭찬을 받은 정도의 합`과 같음
