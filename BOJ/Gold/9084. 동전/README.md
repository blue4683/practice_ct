# BAEKJOON ONLINE JUDGE - 9084. 동전

- [문제출처](https://www.acmicpc.net/problem/9084 '9084. 동전')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 배낭 문제

## 풀이

### 접근

- `DP`

### 점화식

```python

for coin in coins:
    for value in range(1, m + 1):
        if value - coin < 0:
            continue

        dp[value] += dp[value - coin]

```

### 설계

- 현재 가격에서 사용할 동전의 가치를 뺏을 때의 경우의 수를 더해주며 배열에 저장
