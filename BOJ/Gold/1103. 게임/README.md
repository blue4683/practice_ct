# BAEKJOON ONLINE JUDGE - 1103. 게임

- [문제출처](https://www.acmicpc.net/problem/1103 '1103. 게임')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 깊이 우선 탐색

## 풀이

### 접근

- `DFS` + `DP`

### 점화식

```python

def dfs(y, x):
    if out_of_range(y, x):
        return 0

    if visited[y][x]:
        print(-1)
        exit()

    if dp[y][x] != -1:
        return dp[y][x]

    visited[y][x] = 1
    result = -INF
    k = int(arr[y][x])
    for dy, dx in d:
        yy, xx = y + k * dy, x + k * dx
        result = max(result, dfs(yy, xx) + 1)

    dp[y][x] = result
    visited[y][x] = 0
    return dp[y][x]

```

### 설계

- DFS로 이동하는 경우를 탐색하고 방문 체크를 함
- 방문 체크한 곳을 다시 방문하는 경우 루프가 발생하므로 `-1`을 출력하고 실행을 종료시킴
