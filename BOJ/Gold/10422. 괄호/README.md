# BAEKJOON ONLINE JUDGE - 10422. 괄호

- [문제출처](https://www.acmicpc.net/problem/10422 '10422. 괄호')

## 알고리즘 분류

- 수학
- 다이나믹 프로그래밍
- 조합론

## 풀이

### 접근

- `DP`

### 점화식

```python

dp[0] = 1
dp[1] = 1
for i in range(2, 2501):
    for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j]
        dp[i] %= MOD

```

### 설계

- 괄호가 `n`쌍일 때 괄호 1쌍을 기준으로 괄호 쌍들을 안에 넣는 경우와 밖에 넣는 경우의 곱의 합이 괄호 문자열 경우의 수와 같음

### 참고

- [카탈란 수](https://m.blog.naver.com/pyw0564/221523147108)
