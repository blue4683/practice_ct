# BAEKJOON ONLINE JUDGE - 2159. 케익 배달

- [문제출처](https://www.acmicpc.net/problem/2159 '2159. 케익 배달')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n):
    y, x = pos[i]
    for j in range(5):
        dy, dx = d[j]
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx):
            continue

        if not i:
            dp[i][j] = min(dp[i][j], get_distance(sy, sx, yy, xx))
            continue

        for k in range(5):
            ddy, ddx = d[k]
            yyy, xxx = pos[i - 1][0] + ddy, pos[i - 1][1] + ddx
            if out_of_range(yyy, xxx):
                continue

            dp[i][j] = min(dp[i][j], dp[i - 1][k] +
                           get_distance(yy, xx, yyy, xxx))

```

### 설계

- 고객들의 좌표와 그 주변으로 가는 이동거리의 최솟값을 구하고 이를 dp배열에 저장
