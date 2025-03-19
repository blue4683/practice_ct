# BAEKJOON ONLINE JUDGE - 2186. 문자판

- [문제출처](https://www.acmicpc.net/problem/2186 '2186. 문자판')

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

def dfs(y, x, depth):
    if dp[y][x][depth] != -1:
        return dp[y][x][depth]

    if depth == l - 1:
        return 1

    cnt = 0
    for dk in range(1, k + 1):
        for dy, dx in d:
            yy, xx = y + dy * dk, x + dx * dk
            if out_of_range(yy, xx) or arr[yy][xx] != word[depth + 1]:
                continue

            cnt += dfs(yy, xx, depth + 1)

    dp[y][x][depth] = cnt
    return dp[y][x][depth]

```

### 설계

- 시작 알파벳에서 시작해 DFS로 탐색하며 가능한 경우를 dp테이블에 저장
  - 같은 곳을 방문할 수 있으며, 같은 알파벳이 여러개 존재할 수 있으므로 문자의 위치 인덱스에 경우의 수를 저장할 수 있도록 3차원 dp 테이블 생성
