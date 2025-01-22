# BAEKJOON ONLINE JUDGE - 2482. 색상환

- [문제출처](https://www.acmicpc.net/problem/2482 '2482. 색상환')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def get_case(n, k):
    if n / k == 2:
        return 2

    if k == 1:
        return n

    if not dp[n][k]:
        dp[n][k] = (get_case(n - 1, k) + get_case(n - 2, k - 1)) % MOD

    return dp[n][k]
```

### 설계

- `n`개의 색깔 중 `k`개를 선택하는 경우는 `n - 1`개의 색깔 중 `k`개를 선택하는 경우와 `n - 2`개의 색깔 중 `k - 1`개를 선택하는 경우를 더한 것과 같음
