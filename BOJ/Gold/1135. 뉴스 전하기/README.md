# BAEKJOON ONLINE JUDGE - 1135. 뉴스 전하기

- [문제출처](https://www.acmicpc.net/problem/1135 '1135. 뉴스 전하기')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그리디 알고리즘
- 정렬
- 트리
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- 정렬 + `DP`

### 점화식

```python

def dfs(now):
    hour = 0
    next = []

    for node in graph[now]:
        next.append(dfs(node))

    next.sort(reverse=True)
    for i in range(len(next)):
        hour = max(hour, next[i] + i)

    return hour + 1


```

### 설계

- 자식 노드들에게 전파하는데 걸리는 총 시간을 비교
- `Bottom-up` 방식으로 한 노드의 자식 노드들이 전파하는데 걸리는 시간들을 구한 뒤 오래 걸리는 노드 순으로 전파를 시작
  - 노드에 전파할 때마다 시간이 지나므로 `1` 씩 증가를 하고 전파한 뒤 가장 오래 걸리는 시간이 현재 노드의 걸리는 시간
