# BAEKJOON ONLINE JUDGE - 2157. 여행

- [문제출처](https://www.acmicpc.net/problem/2157 '2157. 여행')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(depth, now):
    if now == n:
        return 0

    if depth == m:
        return -10 ** 9

    if dp[now][depth] != -10 ** 9:
        return dp[now][depth]

    for node in range(now + 1, n + 1):
        if not graph[now][node]:
            continue

        dp[now][depth] = max(dp[now][depth], dfs(
            depth + 1, node) + graph[now][node])

    return dp[now][depth]

```

### 설계

- `m`개의 도시를 거치면서(출발, 도착 포함) 점수를 dp배열에 저장하고 탐색에 사용
- dp배열을 최솟값으로 초기화해 불가능한 경우가 업데이트 되는 경우 방지
