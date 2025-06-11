# BAEKJOON ONLINE JUDGE - 12996. Acka

- [문제출처](https://www.acmicpc.net/problem/12996 '12996. Acka')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def solution(depth, a, b, c):
    if not depth:
        return 1 if (a, b, c) == (0, 0, 0) else 0

    if a < 0 or b < 0 or c < 0 or (a + b + c) < depth:
        return 0

    if dp[depth][a][b][c] != -1:
        return dp[depth][a][b][c]

    result = 0
    for dd in d:
        aa = a - 1 if 0 in dd else a
        bb = b - 1 if 1 in dd else b
        cc = c - 1 if 2 in dd else c
        result += solution(depth - 1, aa, bb, cc)
        result %= MOD

    dp[depth][a][b][c] = result
    return result

```

### 설계

- 4차원 배열을 만든 뒤 하나의 곡에 녹음할 수 있는 경우의 수를 탐색
