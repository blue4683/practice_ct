# BAEKJOON ONLINE JUDGE - 1890. 점프

- [문제출처](https://www.acmicpc.net/problem/1890 '1890. 점프')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for y in range(n):
    for x in range(n):
        k = arr[y][x]
        if not k:
            continue

        yy, xx = y + k, x + k
        if not out_of_range(yy, x):
            dp[yy][x] += dp[y][x]

        if not out_of_range(y, xx):
            dp[y][xx] += dp[y][x]

```

### 설계

- 위에서부터 차례대로 탐색하며 갈 수 있는 경우를 배열에 저장
