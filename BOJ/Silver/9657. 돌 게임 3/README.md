# BAEKJOON ONLINE JUDGE - 9657. 돌 게임 3

- [문제출처](https://www.acmicpc.net/problem/9657 '9657. 돌 게임 3')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 게임 이론

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(5, n + 1):
    if 0 in [dp[i - 1], dp[i - 3], dp[i - 4]]:
        dp[i] = 1

    else:
        dp[i] = 0

```

### 설계

- 상근이가 이길 수 있는 경우를 테이블에 저장
