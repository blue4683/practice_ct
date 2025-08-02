# BAEKJOON ONLINE JUDGE - 17070. 파이프 옮기기 1

- [문제출처](https://www.acmicpc.net/problem/17070 '17070. 파이프 옮기기 1')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for y in range(n):
    for x in range(n):
        if arr[y][x] or (y, x) == (0, 0):
            continue

        for i in range(3):
            if i == 1 and (arr[y - 1][x] or arr[y][x - 1]):
                continue

            for j in range(3):
                if abs(i - j) == 2:
                    continue

                dy, dx = d[i]
                yy, xx = y - dy, x - dx
                if yy < 0 or xx < 0:
                    continue

                dp[y][x][i] += dp[yy][xx][j]

```

### 설계

- y, x, 방향을 인덱스로하는 3차원 dp 배열 생성
- 벽을 탐색하거나 대각선 방향으로 진행할 때 왼쪽과 위에 벽이 존재하는 경우는 건너뜀
