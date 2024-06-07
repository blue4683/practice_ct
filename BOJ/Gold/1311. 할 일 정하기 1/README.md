# BAEKJOON ONLINE JUDGE - 1311. 할 일 정하기 1

- [문제출처](https://www.acmicpc.net/problem/1311 '1311. 할 일 정하기 1')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 비트마스킹
- 비트필드를 이용한 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + 비트마스킹

### 점화식

```python

def give(now, status):
    if now == n:
        return 0

    if dp[status] != INF:
        return dp[status]

    dp[status] = INF
    for i in range(n):
        if status & (1 << i) == 0:
            dp[status] = min(dp[status], arr[now][i] +
                             give(now + 1, status | (1 << i)))

    return dp[status]

```

### 설계

- `status`에 일이 할당된 상태를 비트로 저장한 뒤 `now`번째 사람에게 할당되지 않은 일을 시킬것인지 확인
