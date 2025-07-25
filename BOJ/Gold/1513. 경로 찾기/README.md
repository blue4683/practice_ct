# BAEKJOON ONLINE JUDGE - 1513. 경로 찾기

- [문제출처](https://www.acmicpc.net/problem/1513 '1513. 경로 찾기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def bfs():
    visited = [[[[0] * (c + 2) for _ in range(c + 1)]
                for _ in range(m)] for _ in range(n)]
    if arr[0][0]:
        q = deque([(0, 0, 1, arr[0][0])])
        visited[0][0][1][arr[0][0]] = 1
        dp[0][0][1][arr[0][0]] = 1

    else:
        q = deque([(0, 0, 0, 0)])
        visited[0][0][0][0] = 1
        dp[0][0][0][0] = 1

    while q:
        y, x, cnt, before = q.popleft()
        if (y, x) == (n - 1, m - 1):
            continue

        for dy, dx in [(0, 1), (1, 0)]:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            if not arr[yy][xx]:
                dp[yy][xx][cnt][before] += dp[y][x][cnt][before]
                dp[yy][xx][cnt][before] %= MOD
                if not visited[yy][xx][cnt][before]:
                    visited[yy][xx][cnt][before] = 1
                    q.append((yy, xx, cnt, before))

            elif before < arr[yy][xx] and cnt < c:
                dp[yy][xx][cnt + 1][arr[yy][xx]] += dp[y][x][cnt][before]
                dp[yy][xx][cnt + 1][arr[yy][xx]] %= MOD
                if not visited[yy][xx][cnt + 1][arr[yy][xx]]:
                    visited[yy][xx][cnt + 1][arr[yy][xx]] = 1
                    q.append((yy, xx, cnt + 1, arr[yy][xx]))

```

### 설계

- `y, x, 방문한 오락실의 개수, 직전에 방문한 오락실의 번호`를 인덱스로 하는 4차원 dp 배열을 생성
- BFS로 이동하는 경우를 탐색
