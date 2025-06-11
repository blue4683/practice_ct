# BAEKJOON ONLINE JUDGE - 2281. 데스노트

- [문제출처](https://www.acmicpc.net/problem/2281 '2281. 데스노트')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def solution(y, x):
    if y == n:
        return 0

    if dp[y][x] != -1:
        return dp[y][x]

    result = (m - x + 1) ** 2 + solution(y + 1, arr[y] + 1)
    if x + arr[y] <= m:
        result = min(result, solution(y + 1, x + arr[y] + 1))

    dp[y][x] = result
    return dp[y][x]

```

### 설계

- 이름을 다음 줄에 적는 방법과 가능할 경우 이번 줄에 이어 적는 경우 중 최솟값을 dp 테이블에 저장
