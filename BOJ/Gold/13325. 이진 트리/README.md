# BAEKJOON ONLINE JUDGE - 13325. 이진 트리

- [문제출처](https://www.acmicpc.net/problem/13325 '13325. 이진 트리')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 트리
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(node):
    global result
    l, r = node * 2, node * 2 + 1
    if l > n:
        return 0

    left_sum = dfs(l) + graph[l]
    right_sum = dfs(r) + graph[r]

    diff = abs(left_sum - right_sum)
    result += diff

    return max(left_sum, right_sum)

```

### 설계

- 주어진 배열을 트리로 사용하기 위해 앞에 0 두개를 추가
  - 루트 노드가 0이고 루트 노드를 포함하지 않았기 때문에 두개를 추가
- 기존 트리의 전체 합에서 리프까지의 각 경로들의 길이가 같도록 가중치를 더해줌
