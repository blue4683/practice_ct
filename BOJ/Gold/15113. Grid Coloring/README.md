# BAEKJOON ONLINE JUDGE - 15113. Grid Coloring

- [문제출처](https://www.acmicpc.net/problem/15113 '15113. Grid Coloring')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for x in range(n):
    tmp = [0] * (m + 1)
    big = 0
    for y in range(m):
        if grid[y][x] == 'B':
            big = y + 1

    small = m
    for y in range(m - 1, -1, -1):
        if grid[y][x] == 'R':
            small = y

    for y in range(m, -1, -1):
        if y < m:
            dp[y] += dp[y + 1]

        if y >= big and y <= small:
            tmp[y] = dp[y]

    dp = tmp

```
