# BAEKJOON ONLINE JUDGE - 2229. 조 짜기

- [문제출처](https://www.acmicpc.net/problem/2229 '2229. 조 짜기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for e in range(n):
    for s in range(e):
        dp[e] = max(dp[e], dp[s] + diff[s + 1][e])

    dp[e] = max(dp[e], dp[e - 1], diff[0][e])

```

### 설계

- 구간마다 `최댓값 - 최솟값`을 저장하는 이차원 배열 생성
- 위에서 구한 구간을 조합해 `0 ~ n` 범위를 만들면서 최댓값이 되는 경우를 구함
