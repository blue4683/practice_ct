# BAEKJOON ONLINE JUDGE - 11727. 2×n 타일링 2

- [문제출처](https://www.acmicpc.net/problem/11727 '11727. 2×n 타일링 2')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

```

### 설계

- 1칸을 채우는 방법은 1개, 2칸을 채우는 방법은 1칸짜리 두개로 채우는 중복을 제외하고 2개
