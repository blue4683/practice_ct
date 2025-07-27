# BAEKJOON ONLINE JUDGE - 1577. 도로의 개수

- [문제출처](https://www.acmicpc.net/problem/1577 '1577. 도로의 개수')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp[0][0] = 1
for y in range(m + 1):
    for x in range(n + 1):
        if (y, x) == (0, 0):
            continue

        if y and not impossible[((y - 1, x), (y, x))]:
            dp[y][x] += dp[y - 1][x]

        if x and not impossible[((y, x - 1), (y, x))]:
            dp[y][x] += dp[y][x - 1]

```

### 설계

- 이차원 dp 배열을 생성하고 이동 가능한 경우를 업데이트하며 탐색
