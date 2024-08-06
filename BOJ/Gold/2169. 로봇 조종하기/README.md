# BAEKJOON ONLINE JUDGE - 2169. 로봇 조종하기

- [문제출처](https://www.acmicpc.net/problem/2169 '2169. 로봇 조종하기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python
for x in range(1, m):
    dp[0][x] += dp[0][x - 1]

for y in range(1, n):
    left_to_right = dp[y][:]
    right_to_left = dp[y][:]
    for x in range(m - 1, -1, -1):
        if x == m - 1:
            right_to_left[x] += dp[y - 1][x]

        else:
            right_to_left[x] += max(dp[y - 1][x], right_to_left[x + 1])

    for x in range(m):
        if x == 0:
            left_to_right[x] += dp[y - 1][x]

        else:
            left_to_right[x] += max(dp[y - 1][x], left_to_right[x - 1])

    for x in range(m):
        dp[y][x] = max(left_to_right[x], right_to_left[x])
```

### 설계

- `y`가 `0`인 행은 오른쪽으로만 이동할 수 있으므로 더해줌
- `y`가 `1`부터 `n`까지 왼쪽으로 이동하는 경우와 오른쪽으로 이동하는 경우를 나누어 리스트에 저장
  - `x`를 `0`부터 `m`까지 모두 순회한 뒤에 두 경우 중 더 큰 값을 `dp` 테이블에 저장
