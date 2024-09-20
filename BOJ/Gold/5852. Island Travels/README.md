# BAEKJOON ONLINE JUDGE - 5852. Island Travels

- [문제출처](https://www.acmicpc.net/problem/5852 '5852. Island Travels')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 비트마스킹
- 최단 경로
- 다익스트라
- 비트필드를 이용한 다이나믹 프로그래밍
- 외판원 순회 문제

## 풀이

### 접근

- `BFS` + 다익스트라 + 비트마스킹 + `DP`

### 점화식

```python

def get_swim(now, bit):
    if dp[now][bit]:
        return dp[now][bit]

    if bit == all_travel:
        dp[now][bit] = 0
        return dp[now][bit]

    result = INF
    for i in range(1, n + 1):
        if now == i or bit & (1 << i):
            continue

        result = min(result, get_swim(
            i, bit | (1 << i)) + graph[now][i])

    dp[now][bit] = result
    return dp[now][bit]

```

### 설계

- 섬에 번호를 매겨 섬끼리 구분
- 섬끼리 수영으로 갈 수 있는 최단 거리를 구해서 그래프에 저장
  - 최단 거리를 탐색할 때 힙을 사용한 다익스트라 BFS를 활용(시간 복잡도 개선)
- 섬을 방문했다는 것을 비트에 저장해서 최단 거리를 DP 테이블에 저장하면서 최솟값 출력
