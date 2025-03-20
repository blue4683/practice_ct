# BAEKJOON ONLINE JUDGE - 10217. KCM Travel

- [문제출처](https://www.acmicpc.net/problem/10217 '10217. KCM Travel')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 최단 경로
- 다익스트라

## 풀이

### 접근

- `BFS` + `DP`

### 점화식

```python

def bfs():
    result = INF
    q = deque([(1, 0)])
    while q:
        x, c = q.popleft()
        for xx, cc, tt in graph[x]:
            if c + cc > m or dp[xx][c + cc] <= dp[x][c] + tt or dp[x][c] + tt >= result:
                continue

            dp[xx][c + cc] = dp[x][c] + tt
            if xx == n:
                result = min(result, dp[xx][c + cc])
                break

            for i in range(c + cc + 1, m + 1):
                if dp[xx][i] <= dp[xx][c + cc]:
                    break

                dp[xx][i] = dp[xx][c + cc]

            q.append((xx, c + cc))

    return result if result != INF else 'Poor KCM'

```

### 설계

- 공항과 비용을 인덱스로 하는 dp테이블 생성
- BFS로 탐색하면서 도착할 공항까지의 시간이 최소가 되도록 dp테이블에 저장
  - 최소시간을 업데이트할 때, 도착한 공항까지의 비용보다 크면서 시간도 큰 경우 최소시간으로 모두 업데이트(현재비용보다 크면서 시간도 큰 경우는 필요없으므로 탐색에서 제외하기 위해)
