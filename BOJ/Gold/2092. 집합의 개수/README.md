# BAEKJOON ONLINE JUDGE - 2092. 집합의 개수

- [문제출처](https://www.acmicpc.net/problem/2092 '2092. 집합의 개수')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[0] * (a + 1) for _ in range(t + 1)]
size = 0
for i in range(1, t + 1):
    if not cnt[i]:
        for j in range(size + 1):
            dp[i][j] = dp[i - 1][j]

    else:
        if not size:
            for j in range(cnt[i] + 1):
                dp[i][j] += 1
                dp[i][j] %= MOD

            size += cnt[i]

        else:
            for j in range(size + 1):
                for k in range(cnt[i] + 1):
                    dp[i][j + k] += dp[i - 1][j]
                    dp[i][j + k] %= MOD

            size += cnt[i]

```

### 설계

- 각 수의 개수를 카운팅하는 배열을 생성
- 사용하는 숫자와 현재 집합의 크기를 인덱스로 하는 2차원 dp 배열 생성
- 수가 존재하는 경우 이 수를 사용하는 경우를 dp 배열에 업데이트하며 탐색
