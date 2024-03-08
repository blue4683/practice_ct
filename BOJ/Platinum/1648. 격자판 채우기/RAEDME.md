# BAEKJOON ONLINE JUDGE - 1648. 격자판 채우기

- [문제출처](https://www.acmicpc.net/problem/1648 '1648. 격자판 채우기')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 비트마스킹
- 비트필드를 이용한 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + 비트마스킹

### 점화식

```
    if status & 1:
        dp[now][status] = fill(now + 1, status >> 1)

    else:
        dp[now][status] = fill(now + 1, status >> 1 | 1 << (m - 1))
        if now % m != m - 1 and status & 2 == 0:
            dp[now][status] += fill(now + 2, status >> 2)

    dp[now][status] %= 9901
```

### 설계

- `dp[i][j]`: `i`번째 칸을 보고 있는 상태에서 `i`번째 칸부터 `i + m - 1`번째 칸까지 `m`개의 칸의 상태가 `j`일 때 이를 채울 수 있는 방법의 수
  - `j`를 비트필드로 구현
  - `j`의 `n`번째 비트 값은 `i + n - 1`번재 칸이 채워져 있으면 1, 아니면 0으로 구현
- `fill(idx, status)`: `idx ~ idx + m - 1`번째 칸의 상태가 `status`이고 `idx`번째 칸을 채우려고 할 때, 채울 수 있는 방법의 수
  - `2 x 1`크기와 `1 x 2`크기로 채우는 경우를 조건을 통해 판단 후 구현
