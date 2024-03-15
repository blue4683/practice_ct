# BAEKJOON ONLINE JUDGE - 6569. 몬드리안의 꿈

- [문제출처](https://www.acmicpc.net/problem/6569 '6569. 몬드리안의 꿈')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 비트마스킹
- 비트필드를 이용한 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + 비트마스킹

### 점화식

```
if status & (1 << 0):
    dp[idx][status] = fill(idx + 1, status >> 1)

else:
    dp[idx][status] = fill(idx + 1, status >> 1 | 1 << (w - 1))
    if idx % w != w - 1 and status & (1 << 1) == 0:
        dp[idx][status] += fill(idx + 2, status >> 2)
```

### 설계

- `dp[i][j]`: `i`번째 칸을 보고 있는 상태에서 `i`번째 칸부터 `i + w - 1`번째 칸까지 `w`개의 칸의 상태가 `j`일 때 이를 채울 수 있는 방법의 수
  - `j`를 비트필드로 구현
  - `j`의 `w`번째 비트 값은 `i + w - 1`번재 칸이 채워져 있으면 1, 아니면 0으로 구현
- `fill(idx, status)`: `idx ~ idx + w - 1`번째 칸의 상태가 `status`이고 `idx`번째 칸을 채우려고 할 때, 채울 수 있는 방법의 수
  - `2 x 1`크기와 `1 x 2`크기로 채우는 경우를 조건을 통해 판단 후 구현
